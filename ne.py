from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

KV = '''
Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Библиотека"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation:'vertical'
                
                MDLabel:
                	text:'555'
                	padding: [50,0]
                	
                	
                
                OneLineIconListItem:
                	text:'jdjdj'
                	IconLeftWidget:
     				   icon: 'checkbox-marked'
     			
     		   OneLineIconListItem:
                    text:'jdjdj'
                	IconLeftWidget:
     		 	      icon: 'checkbox-marked'
                
                
                ScrollView:
                DrawerList:
          			  
                
              
'''

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass

class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

TestNavigationDrawer().run()