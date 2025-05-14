def set_default_logos():
    import frappe

    try:
        website_settings = frappe.get_doc("Website Settings")
        website_settings.logo = "/assets/commerceflo/images/logo.png"
        website_settings.login_background = "/assets/commerceflo/images/login_background.jpg"
        website_settings.favicon = "/assets/commerceflo/images/logo.png"
        website_settings.save()
        frappe.db.commit()
        print(" Default logos set successfully.")
    except Exception as e:
        print(f" Failed to set default logos: {e}")
