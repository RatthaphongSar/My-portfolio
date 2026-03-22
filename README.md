# 🎨 My Portfolio

Professional web portfolio created with Flask, showcasing skills, projects, and work experience.

## Features

- **Responsive Design** - Dark tech-themed interface with smooth animations
- **Thai Font Support** - Uses Noto Sans Thai for beautiful Thai text rendering
- **Multi-language** - English and Thai content
- **Project Showcase** - Display work experience and projects with highlights
- **Skill Visualization** - Animated skill bars and infrastructure details

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Responsive Design)
- **Fonts**: Barlow, Share Tech Mono, Noto Sans Thai
- **Deployment**: Render.com

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── render.yaml        # Render deployment configuration
└── README.md          # This file
```

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at `http://localhost:5000`

## Deployment on Render

### Step 1: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub account

### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Select repository **`My-portfolio`**

### Step 3: Configure Settings
- **Name**: `my-portfolio`
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Root Directory**: Leave empty or use `.`

### Step 4: Deploy
Click **"Create Web Service"** and wait 1-2 minutes for deployment

### Step 5: Get Your URL
Your portfolio will be live at: `https://my-portfolio-xxxxx.onrender.com`

## Content Structure

### Skills
- **Programming Languages**: C#, Python, JavaScript, SQL
- **Infrastructure**: AWS, Azure, Networking, .NET, Git
- **Database**: Design, Query Optimization, Store Procedure

### Work Experience
- **Company**: qosoft (thailand) co. ltd
- **Position**: Trainee Software support Engineer
- **Responsibilities**: Mobile Service maintenance, SQL scripting, Database management

### Projects
- Server Monitoring System (~16,000 servers)
- Automation Toolkit
- AWS Data Pipeline
- React Dashboard

## Customization

### Update Personal Info
Edit the `portfolio` dictionary in `app.py`:
```python
portfolio = {
    "name": "Your Name",
    "name_th": "ชื่อไทย",
    "role": "Your Role",
    # ... more fields
}
```

### Styling
All CSS is inline in `app.py`. Modify the `<style>` section to customize colors, fonts, and layout.

### Add More Content
Add items to arrays in the `portfolio` dictionary:
- `skills_lang` - Programming skills
- `projects` - Project portfolio
- `strengths` - Core strengths
- `growth` - Learning goals

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This portfolio is for personal use.

## Contact

- Email: rattapong.101@gmail.com
- GitHub: [RatthaphongSar](https://github.com/RatthaphongSar)
- LinkedIn: [Ratthaphong Sar](https://linkedin.com)

---

**Happy sharing! 🚀**
