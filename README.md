# Pomodoro Timer

A simple and effective Pomodoro Technique timer built with Python and Tkinter. This application helps you manage your work sessions and breaks using the proven Pomodoro Technique for enhanced productivity.

## Features

- **Work Sessions**: 25-minute focused work periods (customizable)
- **Short Breaks**: 5-minute breaks between work sessions
- **Long Breaks**: 20-minute breaks after every 4 work sessions
- **Visual Progress**: Checkmarks (✔) appear after each completed work session
- **Audio Notifications**: MP3 sound plays when each session starts
- **Clean UI**: Tomato-themed interface with intuitive controls
- **Session Tracking**: Visual representation of completed work sessions

## Screenshots

The application features a clean, minimalist design with:
- Timer display on a tomato image
- Start and Reset buttons
- Session type indicator (Work/Break)
- Progress checkmarks

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jadarko55/Pomodoro-timer.git
   cd Pomodoro-timer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.6 or higher
- pygame (for audio notifications)
- tkinter (usually comes with Python)

## File Structure

```
Pomodoro-timer/
├── main.py              # Main application file
├── tomato.png           # Tomato image for the UI
├── censor-beep.mp3      # Audio notification sound
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## How to Use

1. **Start a Session**: Click the "Start" button to begin your first work session
2. **Work Focus**: Work for 25 minutes (or your custom duration)
3. **Take Breaks**: The app automatically transitions to break periods
4. **Track Progress**: Watch checkmarks appear after each completed work session
5. **Reset**: Click "Reset" to start over at any time

## The Pomodoro Technique

The Pomodoro Technique is a time management method developed by Francesco Cirillo:

1. **Work** for 25 minutes
2. **Short break** for 5 minutes
3. Repeat steps 1-2 three more times
4. **Long break** for 20 minutes
5. Repeat the entire process

## Customization

You can easily customize the timer durations by modifying these constants in `main.py`:

```python
WORK_MIN = 25          # Work session duration
SHORT_BREAK_MIN = 5    # Short break duration
LONG_BREAK_MIN = 20    # Long break duration
```

## Audio Notification

The app uses `censor-beep.mp3` for session start notifications. You can replace this file with any MP3 of your choice, just make sure to keep the same filename or update the code accordingly.

## Troubleshooting

**Sound not playing?**
- Ensure `censor-beep.mp3` is in the same folder as `main.py`
- Check that pygame is properly installed: `pip install pygame`
- Verify your system's audio is working

**Image not showing?**
- Ensure `tomato.png` is in the same folder as `main.py`
- Check file permissions

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**jadarko55** - [GitHub Profile](https://github.com/jadarko55)

---

*Happy productivity! 🍅⏰*