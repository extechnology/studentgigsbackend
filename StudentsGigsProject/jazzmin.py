

JAZZMIN_SETTINGS = {
    "site_title": "StudentGigs Admin",
    "site_header": "StudentGigs Admin",
    "site_brand": "StudentGigs.com",
    
    
    "site_logo": "./logos/icon.png",  # Path to your site logo
    "login_logo": "./logos/logos1.png",  # Logo for the login page
    "login_logo_dark": "./logos/logos1.png",  # Dark mode logo for the login page
    "site_icon": './logos/icon.png',  # Favicon for your site
    "user_avatar": './logos/icon.png',  # User avatar (can be a path to an image)
    
    "site_logo_classes": " shadow-none d-flex justify-content-center  ",  # Classes for the logo (e.g., background color)
    "login_logo_classes": "shadow-none w-100 ",  # Classes for the logo in the login page
    "login_logo_dark_classes": "shadow-none  w-100",  # Classes for the logo in the login page
    
    
    "welcome_sign": "Welcome to the StudentGigs",
    "copyright": "Acme Ltd",
    "search_model": "auth.User",
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["is_admin"]},
        {"model": "auth.User"},
        {"app": "StudentGigsApp"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
}

JAZZMIN_SETTINGS["show_ui_builder"] = True

