from kivy.uix.textinput import Texture
from kivymd.uix.behaviors.toggle_behavior import MDRaisedButton
from kivymd.uix.button import MDTextButton
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.navigationdrawer.navigationdrawer import NavigationDrawerContentError
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.metrics import dp
from kivymd.uix.fitimage import FitImage # Import FitImage

# Define the KivyMD layout for all screens
KV = """
<WelcomeScreen>:
    name: 'welcome'
    md_bg_color: '#E0BBE4' # Light Purple

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(20)
        
        MDLabel:
            text: "Welcome\\nto HYU\\nCommunity"
            font_size: dp(45)
            bold: True
            color: '#1A1A1A' # Dark text
            halign: 'center'
            valign: 'top'
            size_hint_y: None
            height: self.texture_size[1]
            adaptive_height: True

        FitImage: # Use FitImage to fit the illustration
            source: 'welcome.jpg' # Update this path
            size_hint_y: 1

        MDBoxLayout:
            size_hint_y: None
            height: dp(60)
            MDRaisedButton:
                text: "Next"
                font_size: dp(18)
                bold: True
                md_bg_color: '#1A1A1A' # Dark button background
                text_color: '#FFFFFF' # White text
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: app.root.current = 'support'
                size_hint_x: 0.8
                height: dp(50)


<SupportScreen>:
    name: 'support'
    md_bg_color: '#FFF7AE' # Light Yellow

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(20)

        MDLabel:
            text: "Get support\\nin your\\nnew career"
            font_size: dp(45)
            bold: True
            color: '#1A1A1A' # Dark text
            halign: 'center'
            valign: 'top'
            size_hint_y: None
            height: self.texture_size[1]
            adaptive_height: True

        FitImage: # Use FitImage for the illustration
            source: 'assets/screen2_illustration.png' # Update this path
            size_hint_y: 1

        MDBoxLayout:
            size_hint_y: None
            height: dp(60)
            MDRaisedButton:
                text: "Next"
                font_size: dp(18)
                bold: True
                md_bg_color: '#1A1A1A' # Dark button background
                text_color: '#FFFFFF' # White text
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: app.root.current = 'login'
                size_hint_x: 0.8
                height: dp(50)

<LoginScreen>:
    name: 'login'
    md_bg_color: '#1A1A1A' # Black background

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(40)
        spacing: dp(30)
        
        MDLabel:
            text: "Hello\\nagain!"
            font_size: dp(45)
            bold: True
            color: '#FFFFFF' # White text
            halign: 'center'
            valign: 'top'
            size_hint_y: None
            height: self.texture_size[1]
            adaptive_height: True
            
        MDTextField:
            id: email_field
            hint_text: "User Name"
            mode: "rectangle"
            line_color_normal: '#505050' # Dark grey line
            line_color_focus: '#FFF7AE' # Yellow focus line
            text_color_normal: '#FFFFFF' # White text
            text_color_focus: '#FFFFFF' # White text
            hint_text_color_normal: '#AAAAAA' # Lighter grey hint
            hint_text_color_focus: '#FFF7AE' # Yellow hint on focus
            color_mode: 'custom'
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.9
            current_hint_text_color: '#FFF7AE' # Ensure hint text matches focus color if custom
            
        MDTextField:
            id: password_field
            hint_text: "Password"
            mode: "rectangle"
            password: True # Masks the input
            line_color_normal: '#505050'
            line_color_focus: '#FFF7AE'
            text_color_normal: '#FFFFFF'
            text_color_focus: '#FFFFFF'
            hint_text_color_normal: '#AAAAAA'
            hint_text_color_focus: '#FFF7AE'
            color_mode: 'custom'
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.9
            current_hint_text_color: '#FFF7AE'
            
        MDBoxLayout:
            size_hint_y: None
            height: dp(60)
            MDRaisedButton:
                text: "Log in"
                font_size: dp(18)
                bold: True
                md_bg_color: '#FFF7AE' # Yellow button background
                text_color: '#1A1A1A' # Dark text
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_release: root.login_user(email_field.text, password_field.text) # Example login call
                size_hint_x: 0.9
                height: dp(50)

        MDLabel:
            text: "I don't have an account"
            color: '#FFFFFF' # White text
            halign: 'center'
            font_size: dp(14)
            size_hint_y: None
            height: self.texture_size[1]

        MDTextButton:
            text: "Sign up >"
            color: '#FFFFFF' # White text
            font_size: dp(16)
            bold: True
            halign: 'center'
            on_release: print("Sign up clicked") # Placeholder for sign up action
            size_hint_y: None
            height: self.texture_size[1]
            on_release: app.root.current = 'Signup'
            
            
<SignUpPage>:
    name: 'Signup'
    md_bg_color: '#1A1A1A'

    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(20)
            size_hint_y: None
            height: self.minimum_height  # Makes BoxLayout as tall as its children
            pos_hint: {'top': 1}  # Ensures it's pinned to top in ScrollView

            MDLabel:
                text: "Join With Us\\nLearn New"
                font_size: dp(45)
                bold: True
                color: '#FFFFFF'
                halign: 'center'
                valign: 'top'
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: signup_email
                hint_text: 'User Email'
                mode: 'rectangle'
                line_color_normal: '#505050'
                line_color_focus: '#FFF7AE'
                text_color_normal: '#FFFFFF'
                text_color_focus: '#FFFFFF'
                hint_text_color_normal: '#AAAAAA'
                hint_text_color_focus: '#FFF7AE'
                color_mode: 'custom'
                pos_hint: {'center_x': 0.5}
                size_hint_x: 0.9
                current_hint_text_color: '#FFF7AE'

            MDTextField:
                id: sign_pass
                hint_text: 'Password'
                mode: 'rectangle'
                line_color_normal: '#505050'
                line_color_focus: '#FFF7AE'
                text_color_normal: '#FFFFFF'
                text_color_focus: '#FFFFFF'
                hint_text_color_normal: '#AAAAAA'
                hint_text_color_focus: '#FFF7AE'
                color_mode: 'custom'
                pos_hint: {'center_x': 0.5}
                size_hint_x: 0.9
                current_hint_text_color: '#FFF7AE'

            MDTextField:
                id: User_Name
                hint_text: 'Username'
                mode: 'rectangle'
                line_color_normal: '#505050'
                line_color_focus: '#FFF7AE'
                text_color_normal: '#FFFFFF'
                text_color_focus: '#FFFFFF'
                hint_text_color_normal: '#AAAAAA'
                hint_text_color_focus: '#FFF7AE'
                color_mode: 'custom'
                pos_hint: {'center_x': 0.5}
                size_hint_x: 0.9
                current_hint_text_color: '#FFF7AE'

            MDBoxLayout:
                size_hint_y: None
                height: dp(60)
                spacing: dp(40)
                padding: dp(10)
                MDRaisedButton:
                    text: 'Enjoy Career'
                    md_bg_color: '#FFF7AE'
                    bold: True
                    pos_hint: {'center_x': 0.5}
                    font_size: dp(18)
                    text_color: '#1A1A1A'
                    size_hint_x: 0.9
                    height: dp(50)
                    on_release: app.root.current = 'login' 
                
                
            
        
"""

class WelcomeScreen(MDScreen):
    pass

class SupportScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    def login_user(self, email, password):
        # This is a placeholder for your login logic
        print(f"Attempting to log in with Email: {email}, Password: {password}")
        if email == "karthik@gmail.com" and password == "password": # Example credentials
            print("Login Successful!")
            # app.root.current = 'dashboard' # Transition to a dashboard screen if you have one
        else:
            print("Invalid credentials.")
            # You might want to show a toast or dialog for invalid login
class SignUpPage(MDScreen):
    pass
class HYUApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" # You can choose "Light" or "Dark" as overall theme
        self.theme_cls.primary_palette = "BlueGray" # Primary palette won't affect custom colors much here

        screen_manager = MDScreenManager()
        screen_manager.add_widget(WelcomeScreen()) # Added back for full flow
        screen_manager.add_widget(SupportScreen()) # Added back for full flow
        screen_manager.add_widget(LoginScreen())
        screen_manager.add_widget(SignUpPage())
        return screen_manager

if __name__ == '__main__':
    # Load the KV string builder here
    Builder.load_string(KV)
    HYUApp().run()
