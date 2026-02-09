# Portfolio Website

A modern, easy-to-customize portfolio website built with Flask. This website is designed to showcase your skills, projects, and experience in a professional manner.

## Features

- **Easy Configuration**: All personal information, projects, and content managed through a single `config.json` file
- **Data Storage**: SQLite database for storing contact messages, projects, and other dynamic content
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Multiple Pages**: Home, About, Projects, Contact, and Shop pages
- **Contact Form**: Functional contact form with database storage
- **Dynamic Navigation**: Navigation menu automatically generated from configuration
- **Project Showcase**: Display your projects with images, descriptions, and links
- **Skills & Experience**: Show your skills with visual progress bars and work history

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/theYockaman/portfolio-website.git
cd portfolio-website

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Edit the `config.json` file to customize your portfolio:

```json
{
  "site": {
    "title": "Your Name",
    "description": "Your portfolio description"
  },
  "personal": {
    "name": "Your Name",
    "title": "Your Title",
    "bio": "Your bio",
    "email": "your@email.com"
  },
  "projects": [
    {
      "title": "Project Name",
      "description": "Project description",
      "technologies": ["Python", "Flask"],
      "github": "https://github.com/username/project"
    }
  ]
}
```

### 3. Run the Application

```bash
python main.py
```

Visit `http://localhost:5000` in your browser.

## Configuration Guide

### Site Settings (`config.json`)

#### Site Information
```json
"site": {
  "title": "Your Name",
  "description": "Portfolio Website description",
  "logo": "/static/Content/Icons/wizardLogo.png"
}
```

#### Personal Information
```json
"personal": {
  "name": "Your Name",
  "title": "Software Engineer",
  "bio": "Your professional bio",
  "email": "contact@example.com",
  "phone": "+1 (555) 123-4567",
  "location": "City, Country"
}
```

#### Social Links
```json
"social": {
  "github": "https://github.com/yourusername",
  "linkedin": "https://linkedin.com/in/yourprofile",
  "twitter": "https://twitter.com/yourhandle"
}
```

#### Navigation Menu
```json
"navigation": [
  { "name": "Home", "url": "/" },
  { "name": "About", "url": "/about" },
  { "name": "Projects", "url": "/projects" },
  { "name": "Contact", "url": "/contact" }
]
```

#### Projects
```json
"projects": [
  {
    "id": 1,
    "title": "Project Title",
    "description": "Project description",
    "image": "/static/Content/Images/project1.jpg",
    "technologies": ["Python", "Flask", "JavaScript"],
    "github": "https://github.com/username/project",
    "demo": "https://project-demo.com",
    "featured": true
  }
]
```

#### About Section
```json
"about": {
  "introduction": "Your introduction",
  "skills": [
    { "name": "Python", "level": 90 },
    { "name": "JavaScript", "level": 80 }
  ],
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Company Name",
      "period": "2020 - Present",
      "description": "Job description"
    }
  ],
  "education": [
    {
      "degree": "Computer Science",
      "institution": "University Name",
      "year": "2020"
    }
  ]
}
```

## Adding Images

1. Place your images in the `website/static/Content/Images/` directory
2. Create the directory if it doesn't exist:
   ```bash
   mkdir -p website/static/Content/Images
   ```
3. Reference images in `config.json` using the path:
   ```json
   "image": "/static/Content/Images/your-image.jpg"
   ```

## Customizing Styles

Edit the CSS files in `website/static/CSS/`:
- `reset.css` - Base styles and resets
- `about.css` - About page styles
- `projects.css` - Projects page styles
- `contact.css` - Contact page styles
- `shop.css` - Shop page styles

## Database

The application uses SQLite for data storage. The database includes:
- **ContactMessage**: Stores messages from the contact form
- **Project**: Can store projects (in addition to config.json)
- **Skill**: Store skills and proficiency levels
- **Experience**: Work experience entries
- **User**: For future authentication features

The database is automatically created in the `instance/` directory when you first run the application.

## Project Structure

```
portfolio-website/
├── config.json              # Main configuration file
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── instance/               # Database files (auto-generated)
└── website/
    ├── __init__.py         # Flask app initialization
    ├── views.py            # Route handlers
    ├── models.py           # Database models
    ├── data.py             # Configuration manager
    ├── static/
    │   ├── CSS/           # Stylesheets
    │   ├── JS/            # JavaScript files
    │   └── Content/       # Images and other content
    └── templates/         # HTML templates
        ├── base.html      # Base template
        ├── index.html     # Home page
        ├── about.html     # About page
        ├── projects.html  # Projects page
        ├── contact.html   # Contact page
        └── shop.html      # Shop page
```

## Making Changes

### To Update Personal Information:
1. Edit `config.json`
2. Update the `personal` section
3. Restart the application

### To Add a New Project:
1. Add your project to the `projects` array in `config.json`
2. Add project image to `website/static/Content/Images/`
3. Restart the application

### To Change Navigation:
1. Edit the `navigation` array in `config.json`
2. Restart the application

## Reference Websites

Example portfolios for inspiration:
- https://stevewolf.co/
- https://brittanychiang.com/
- https://www.adhamdannaway.com/
- https://benadam.me/

## Design Ideas Implemented

- ✅ Easy to update personal information
- ✅ Projects showcase
- ✅ About me page with skills and experience
- ✅ Contact form with database storage
- ✅ Social media links
- ✅ Professional navigation
- ✅ Responsive design
- ✅ Data storage for contact messages

## Future Enhancements

- Shop functionality
- Blog section
- User authentication
- Admin panel for managing content
- Image upload functionality
- Project categories and filtering

## License

This project is open source and available for personal use.

## Support

For questions or issues, please open an issue on GitHub.
