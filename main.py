import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from src.infra.list import GroceryList

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=1, padding=5)
        
        img = Image(source='src/data/img/cartopia6.png', size_hint=(0.5, 0.5))
        
        item_label = Label(text='Item Name:', size_hint=(0.5, None), height=30, halign='left')
        self.item_input = TextInput(multiline=False, size_hint=(0.5, None), height=30)
        
        quantity_label = Label(text='Quantity:', size_hint=(0.5, None), height=30, halign='left')
        self.quantity_input = TextInput(multiline=False, size_hint=(0.5, None), height=30)
        
        add_button = Button(text='Add Item', on_release=self.add_item, size_hint=(0.5, None), height=30)
        display_button = Button(text='Display List', on_release=self.display_list, size_hint=(0.5, None), height=30)
        
        layout.add_widget(img)
        layout.add_widget(item_label)
        layout.add_widget(self.item_input)
        layout.add_widget(quantity_label)
        layout.add_widget(self.quantity_input)
        layout.add_widget(add_button)
        layout.add_widget(display_button)
        
        self.add_widget(layout)
        
    def add_item(self, instance):
        item_name = self.item_input.text
        quantity = self.quantity_input.text
        GroceryList.add_item(item_name, quantity)
        self.item_input.text = ''
        self.quantity_input.text = ''
        
    def display_list(self, instance):
        App.get_running_app().sm.current = 'list'
        
class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=5, padding=5)
        img = Image(source='src/data/img/cartopia3.png', size_hint=(0.5, 0.5)) 
        back_button = Button(text='Back to Main', on_release=self.back_to_main, size_hint=(1, None), height=30)
        delete_item_button = Button(text='Delete', on_release=self.delete_item, size_hint=(1, None), height=30)
        layout.add_widget(back_button)
        
        self.list_label = Label(text='', size_hint=(1, 1))
        layout.add_widget(self.list_label)
        
        self.add_widget(layout)

    def delete_item(self, item):
        GroceryList.delete_item(item)
        self.list_label.text = '\n'.join(GroceryList.get_list())
        
    def on_pre_enter(self):
        self.list_label.text = '\n'.join(GroceryList.get_list())
        
    def back_to_main(self, instance):
        App.get_running_app().sm.current = 'main'
        

class GroceryListApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(ListScreen(name='list'))
        
        return self.sm
    
if __name__ == '__main__':
    GroceryListApp().run()
