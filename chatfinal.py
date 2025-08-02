from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

KV = """
<ChatPage>:
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: 'Ask\\nLearn New'
            font_size: dp(45)
            bold: True
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: None
            height: self.texture_size[1]

        Widget:  
            
            
        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(60)
            spacing: dp(10)
            padding: [dp(10), 0]

            MDTextField:
                id: doubt
                mode: 'rectangle'
                hint_text: "Ask Your Doubt..."
                line_color_normal: '#FFF7AE'
                line_color_focus: '#505050'
                text_color_focus: '#FFFFFF'
                text_color_normal: "#FFFFFF"
                hint_text_color_focus: '#AAAAAA'
                hint_text_color_normal: "#FFF7AF"
                color_mode: 'custom'
                size_hint_x: 0.85
                height: dp(60)
                pos_hint: {'center_y': 0.5}

            MDCard:
                size_hint: None, None
                size: dp(50), dp(50)
                radius: [25, 25, 25, 25]
                md_bg_color: "#ec79e7ff"
                elevation: 6

                MDIconButton:
                    icon: "send"
                    icon_color: "#0a0909ff"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    


"""

class ChatPage(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        
        Builder.load_string(KV)
        
        screen_manager = MDScreenManager()
        screen_manager.add_widget(ChatPage())
        
        return screen_manager
    
if __name__ == "__main__":
    MyApp().run()