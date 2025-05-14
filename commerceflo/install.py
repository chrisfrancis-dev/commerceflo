def set_default_logos():
    import frappe

    try:
        website_settings = frappe.get_doc("Website Settings")
        navbar_settings = frappe.get_doc("Navbar Settings")
        website_settings.app_logo = "/assets/commerceflo/images/logo2.png"
        website_settings.splash_image = "/assets/commerceflo/images/logo2.png"
        website_settings.favicon = "/assets/commerceflo/images/logo.jpeg"
        navbar_settings.app_logo = "/assets/commerceflo/images/logo2.png"
        website_settings.save()
        frappe.db.commit()
        print(" Default logos set successfully.")
    except Exception as e:
        print(f" Failed to set default logos: {e}")
