# Configuration Guide

This guide explains how to customize your portfolio website using the `config.json` file.

## Overview

All the content of your portfolio website is managed through a single `config.json` file located in the root directory. This makes it easy to update your information without touching any code.

## Getting Started

1. Copy `config.example.json` to `config.json` (if you haven't already)
2. Edit `config.json` with your personal information
3. Restart the application to see your changes

```bash
cp config.example.json config.json
# Edit config.json with your favorite editor
python main.py
```

## Configuration Sections

### 1. Site Settings

Basic information about your website:

```json
"site": {
  "title": "Your Name",
  "description": "Portfolio Website - Your Title/Role",
  "logo": "/static/Content/Icons/wizardLogo.png"
}
```

- **title**: Shows in browser tab and page title
- **description**: Meta description for SEO
- **logo**: Path to your logo image (used in navbar and favicon)

### 2. Personal Information

Your basic contact and professional information:

```json
"personal": {
  "name": "Your Full Name",
  "title": "Software Engineer",
  "bio": "Brief professional bio",
  "email": "your.email@example.com",
  "phone": "+1 (555) 123-4567",
  "location": "City, Country",
  "tagline": "Your professional motto"
}
```

This information appears on:
- Contact page
- About page
- Meta tags

### 3. Social Links

Links to your social media profiles:

```json
"social": {
  "github": "https://github.com/yourusername",
  "linkedin": "https://linkedin.com/in/yourprofile",
  "twitter": "https://twitter.com/yourhandle",
  "portfolio": "https://yourportfolio.com"
}
```

These links appear on the contact page.

### 4. Navigation Menu

Customize your site navigation:

```json
"navigation": [
  { "name": "Home", "url": "/" },
  { "name": "About", "url": "/about" },
  { "name": "Projects", "url": "/projects" }
]
```

- The navbar is automatically generated from this array
- You can add, remove, or reorder items
- The "Home" link is automatically excluded from the navbar

### 5. About Section

Detailed information for your About page:

#### Introduction and Image

```json
"about": {
  "image": "/static/Content/Images/profile.jpg",
  "introduction": "Your introduction paragraph..."
}
```

#### Skills

Display your technical skills with proficiency levels:

```json
"skills": [
  { "name": "Python", "level": 90 },
  { "name": "JavaScript", "level": 85 }
]
```

- **name**: Skill name
- **level**: Proficiency level (0-100)
  - Shows as a progress bar on the About page

#### Experience

Your work history:

```json
"experience": [
  {
    "title": "Software Engineer",
    "company": "Tech Company",
    "period": "2020 - Present",
    "description": "What you did in this role"
  }
]
```

#### Education

Your educational background:

```json
"education": [
  {
    "degree": "Computer Science",
    "institution": "University Name",
    "year": "2020",
    "description": "Relevant details"
  }
]
```

### 6. Projects

Showcase your work:

```json
"projects": [
  {
    "id": 1,
    "title": "Project Name",
    "description": "What the project does",
    "image": "/static/Content/Images/project1.jpg",
    "technologies": ["Python", "Flask", "JavaScript"],
    "github": "https://github.com/username/project",
    "demo": "https://demo-url.com",
    "featured": true
  }
]
```

- **id**: Unique identifier (number)
- **title**: Project name
- **description**: Brief explanation
- **image**: Path to project screenshot
- **technologies**: Array of tech stack items
- **github**: Link to source code (optional)
- **demo**: Link to live demo (optional)
- **featured**: If `true`, project is highlighted with a special border

### 7. Contact Settings

Configure the contact page:

```json
"contact": {
  "heading": "Get In Touch",
  "subheading": "Let's work together",
  "form_enabled": true,
  "form_endpoint": "/api/contact"
}
```

- **form_enabled**: Set to `false` to hide the contact form
- Contact form submissions are saved to the database

### 8. Hero Section

Homepage hero/carousel settings:

```json
"hero": {
  "enabled": true,
  "images": [
    "/static/Content/Images/hero1.jpg",
    "/static/Content/Images/hero2.jpg"
  ],
  "slides": [
    {
      "title": "Welcome",
      "description": "Your tagline"
    }
  ]
}
```

- **enabled**: Show/hide hero section
- **images**: Array of hero image paths
- **slides**: Content for each slide

## Working with Images

### Adding Images

1. Place images in: `website/static/Content/Images/`
2. Reference in config using: `/static/Content/Images/filename.jpg`

### Image Guidelines

- **Profile Photo**: 250x250px minimum, square aspect ratio
- **Project Images**: 800x600px or 4:3 ratio
- **Hero Images**: 1920x1080px or 16:9 ratio
- **Formats**: JPG, PNG, GIF, WebP

### Example

```bash
# Add your image
cp ~/my-photo.jpg website/static/Content/Images/profile.jpg

# Update config.json
"about": {
  "image": "/static/Content/Images/profile.jpg"
}
```

## Common Tasks

### Change Your Name

Edit `config.json`:
```json
"personal": {
  "name": "New Name"
}
```

### Add a New Project

Add to the `projects` array in `config.json`:
```json
{
  "id": 3,
  "title": "New Project",
  "description": "Description",
  "image": "/static/Content/Images/newproject.jpg",
  "technologies": ["Tech1", "Tech2"],
  "github": "https://github.com/user/newproject",
  "featured": false
}
```

### Update Skills

Modify the `skills` array in `config.json`:
```json
"skills": [
  { "name": "New Skill", "level": 75 }
]
```

### Change Navigation

Edit the `navigation` array:
```json
"navigation": [
  { "name": "Blog", "url": "/blog" }
]
```

### Hide Contact Form

Set `form_enabled` to false:
```json
"contact": {
  "form_enabled": false
}
```

## Tips

1. **JSON Validation**: Use a JSON validator to check syntax before restarting
2. **Backup**: Keep a backup of `config.json` before major changes
3. **Comments**: JSON doesn't officially support comments, but entries with `_comment` keys are ignored
4. **Restart Required**: Always restart the application after editing `config.json`

## Troubleshooting

### Application Won't Start

- Check JSON syntax with a validator
- Ensure all quotes are properly closed
- Verify no trailing commas in arrays/objects

### Images Not Showing

- Verify image path is correct
- Check image file exists in `website/static/Content/Images/`
- Ensure path starts with `/static/`

### Configuration Not Loading

- Check console for error messages
- Verify `config.json` is in the project root directory
- Ensure file has proper read permissions

## Advanced

### Programmatic Access

In Python code, you can access config values:

```python
from website.data import get_config_manager

config = get_config_manager()
name = config.get('personal.name')
projects = config.get('projects', [])
```

### Updating Configuration

To update config programmatically:

```python
config.update('personal.name', 'New Name')
```

### API Access

Get configuration via API:
```
GET /api/config
```

Returns the entire configuration as JSON.

## Support

If you encounter issues:
1. Check the main README.md
2. Verify all paths and syntax
3. Check console output for error messages
4. Open an issue on GitHub with details
