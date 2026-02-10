# Images Directory

Place your hero section image here.

**Recommended filename:** `hero-portrait.jpg` or `hero-portrait.png`

The image should be:
- A portrait image (half-body or full-body)
- High quality (recommended: 800x1000px or larger)
- Optimized for web (compressed but maintaining quality)

After placing the image, update the template to reference it using:
`{% load static %}`
`<img src="{% static 'myApp/images/hero-portrait.jpg' %}" alt="...">`

