# 📄 Caption Generating Tool: Image Captioning, Object Detection, and Translation App

## 🌟 Project Summary
This is a smart and user-friendly web app built with Streamlit. It allows users to upload an image, automatically generates a detailed description using AI, detects visible objects, translates the caption into different languages, and even reads it aloud using text-to-speech. It's like a multi-tool for understanding images in any language!

We use advanced AI models for captioning and object detection: BLIP for image understanding and YOLOv8 for object detection. This app is helpful for accessibility, language learners, content creators, and more.

---

# 🚀 Real-World Use Cases
Here are some ways this app could be useful:

1. Visually Impaired Assistance
The app can describe what's in an image and read it aloud. This helps people who can't see the image understand what's in it.

2. Learning and Education
It helps students or teachers translate image descriptions into their own language. Great for language learning or understanding visuals.

3. Travel and Tourism
Travelers can upload photos of signs or places and get descriptions in their native language.

4. Social Media & Content Creators
Content creators can auto-generate captions and translate them into multiple languages to reach a global audience.

5. Online Shopping
This app can help sellers describe product images and make the info available to more people in different languages.

6. Surveillance & Security
Security teams can upload footage or snapshots and instantly detect people, cars, or objects in the scene.

7. Hospitals and Healthcare
Used in healthcare to help with basic captioning of medical diagrams or illustrations in multi-language environments.

---

## ⚙️ Development Environment
- **Operating System:** Windows 10 or 11
- **Python Version:** 3.9+
- **Environment:** Virtual Environment (`venv`) used to keep dependencies organized

---

## 🔧 Programming Languages Used
- **Python 3.9+** — for everything in the app, including backend logic, model integration, and UI

---

## 📂 Folder Structure Overview
```
Final-Project/
├── Reference.doc           # All the references we have used
├── README.md               # This documentation file
├── requirements.txt        # All Python libraries needed
├── /images                 # Screenshots from debugging + final results
│   Final output.png
├── /src                   # Source files (like backups or module split files)
│   └── app.py             # Same as main app or experimental version
```

---

# 🛠️ Tools and Libraries Used
| Tool / Library | Purpose | License |
|----------------|---------|---------|
| Streamlit      | UI and web app framework | Apache 2.0 |
| gTTS           | Convert text into speech | Apache 2.0 |
| PyTorch        | Deep learning backend for models | BSD-3 |
| HuggingFace Transformers | Runs BLIP captioning model | Apache 2.0 |
| Ultralytics (YOLOv8) | Object detection in images | GPLv3 |
| deep-translator | Language translation using Google Translate | MIT |
| Pillow         | For handling image files | HPND |

---

# 🔍 What the Tools Did
- **BLIP model** was used to look at the image and generate a sentence that describes it.
- **YOLOv8** detected specific objects in the image, like "car", "person", "dog", etc.
- We combined those two into a final caption: “The image contains a dog and a car. Here's a detailed description: A brown dog is standing beside a red sports car.”
- **gTTS** turned that caption into speech.
- **deep-translator** let us choose another language (like Spanish or Hindi), translated the caption, and we could also hear it spoken aloud.

---

# 📥 How to Install and Run This Project

# Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/language-detector
cd language-detector
```

# Step 2: Set Up the Virtual Environment
```bash
python -m venv myenv
.\myenv\Scripts\activate
```

# Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

# Step 4: Run the App
```bash
streamlit run app.py
```

---

# ⚒️ Commands You Need to Know
To run the app:
```bash
streamlit run app.py
```

To exit the app, press `Ctrl + C` in the terminal.

---

# 🧾 What Happens After Running
The app will:
- Ask the user to upload an image.
- Create 2 MP3 files: `english_description.mp3` and `translated_description.mp3`
- These will appear in the project folder temporarily.
- You can download them from the app directly or move them to `/output/`.

---

# 🧪 Debugging Summary
We encountered the following issues:

# 🔹 YOLOv5 Loading Error
- At first, we tried to use YOLOv5 with the Ultralytics YOLOv8 API, which failed.
- Solution: Switched to `yolov8n`, which worked well and loaded without errors.

# 🔹 Model Download and Caching
- Some models were slow to download and didn’t work on the first try due to network or permission issues.
- Solution: Pre-download the models and cache them before running the app.

# 🔹 TTS File Handling
- There were times where `gTTS` wouldn't save files in OneDrive synced folders.
- Solution: Always run the script from a local, non-cloud path.

We Didnt took any screenshots during these issues So we dont have any pictures of the debugging, But we will be attaching our final input image.

---

# ✅ Final Screenshots (Add Yourself)
Include:
- Final output showing caption + translated version
- Audio playback UI
- Dropdown language list
- Uploaded image and detection box (if added)


# 👥 Team Contribution Summary
| Team Member | Contributions |
|-------------|----------------|
| Garv     | Image Processing and Object Detection |
| Siddhi    | Image Description and Translation |
| Gokulhesh  |Audio Output and User Interface |
| Enosh  | Backend Development and Integration |


---

# 📄 Deliverables List
- [x] `README.md`
- [x] Source code in `/src`
- [x] Final screenshots in `/images`
- [x] `requirements.txt`
- [x] `references.docx` — This file includes a full list of all tools, models, libraries, and websites used in this project along with their official URLs and citations. [x] `README.md`
- [x] Source code in `/src`
- [x] Final screenshots in `/images`
- [x] `requirements.txt`
- [ ] `references.docx` (to be added manually in Word)

---
References

We have added References in APA 7th Format and put in References.docx in the directory , go through it if you are curious


