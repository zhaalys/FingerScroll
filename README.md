# 🖐️ FingerScroll

**Hand-Controlled Screen Scrolling using Computer Vision**

FingerScroll is a lightweight, hands-free scrolling tool that uses your webcam and AI-powered hand tracking to navigate pages. Built with MediaPipe and OpenCV, it translates simple finger gestures into smooth scrolling actions.

---

## ✨ Features

- **Hands-Free Control**: Scroll through recipes, sheet music, or code without touching your mouse.
- **Ultra-Responsive**: Zero-latency scrolling (optimized with custom `pyautogui` settings).
- **Lightweight**: Low CPU usage thanks to efficient MediaPipe tracking.
- **Easy to Use**: No complex setup—just clone and run.

---

## 🎮 How to Use

| Gesture                | Action          |
| :--------------------- | :-------------- |
| **Index Finger Up** ☝️ | **Scroll UP**   |
| **Thumb Down** 👎      | **Scroll DOWN** |
| **Other States** ✊    | **Idle (Stop)** |

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/zhaalys/FingerScroll.git
cd FingerScroll
```

### 2. Set Up Environment (Recommended)

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

---

## ⚙️ Configuration

You can adjust the scrolling sensitivity in `main.py`:

```python
SCROLL_SPEED = 100  # Change this value to adjust speed
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/zhaalys/FingerScroll/issues).

_Created with ❤️ for a better hands-free experience._
