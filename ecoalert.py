from flask import Flask, request, render_template, redirect, url_for, send_file
import openai
import cv2
import time
import os
from datetime import datetime

# OpenAI API setup
# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = 'temp'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to detect specific activities in video frames (Placeholder for detection logic)
def detect_activities_in_video(video_path):
    cap = cv2.VideoCapture(video_path)
    detected_events = []
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Placeholder for real-time activity detection
        if frame_count % 100 == 0:  # For example, every 100th frame has an event
            event_time = frame_count / cap.get(cv2.CAP_PROP_FPS)
            detected_events.append({
                'type': 'Littering' if frame_count % 200 == 0 else 'Urinating',
                'time': event_time
            })

        frame_count += 1

    cap.release()
    return detected_events

# Function to generate voice-over using OpenAI (GPT-3)
def generate_voice_over(event):
    prompt = f"Describe the event of {event['type']} in a public space."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Function to generate a summary report
def generate_summary_report(events):
    report = "Incident Report:\n"
    report += f"Report Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    for event in events:
        event_time = time.strftime("%H:%M:%S", time.gmtime(event['time']))
        report += f"{event['type']} detected at {event_time}\n"
    return report

# Route for uploading and processing videos
@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Save the uploaded file
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(video_path)

            # Detect activities in the video
            detected_events = detect_activities_in_video(video_path)

            # Generate voice-over for each event
            events_with_voice_overs = []
            for event in detected_events:
                voice_over = generate_voice_over(event)
                events_with_voice_overs.append({
                    'type': event['type'],
                    'time': event['time'],
                    'voice_over': voice_over
                })

            # Generate summary report
            summary_report = generate_summary_report(detected_events)

            return render_template('results.html', events=events_with_voice_overs, report=summary_report)

    return render_template('upload.html')

# Route for downloading the summary report
@app.route('/download_report', methods=['POST'])
def download_report():
    report_content = request.form.get('report')
    report_path = os.path.join(app.config['UPLOAD_FOLDER'], 'summary_report.txt')
    with open(report_path, 'w') as f:
        f.write(report_content)
    return send_file(report_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3004, debug=True, use_reloader=False)


