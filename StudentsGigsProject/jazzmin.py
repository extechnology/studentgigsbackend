

JAZZMIN_SETTINGS = {
    "site_title": "StudentGigs Admin",
    "site_header": "StudentGigs",
    "site_brand": "StudentGigs.com",
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


