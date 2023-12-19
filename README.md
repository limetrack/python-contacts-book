# group-8-py-final-prooject
[Python] Address Book Assistant

# Structure:
1. App
- command_bot - processes user inputs
- command_handlers - separate handlers for commands
- Fields, Record, AddressBook - contains classes
2. Utils
- error_handlers - decorators / custom errors for error handling
- prompt_handlers - some helpers for getting user inputs
- validators - fields validators (phone, email, date)
3. Constants
- messages - all messages to print (errors, helpers)

# How to use
``` git clone <repo> ```
- open root terminal or run ``` main.py ``` file
- for your changes:
``` git checkout -b feat/<your_task_goal> ```

# Recomendations
1. Помилки валідації мають оброблятися в класі конкретного поля (Phone, Email, Birthday...)
2. Помилки, повʼязані з конкретним рекордом - в класі Record
3. Помилки, повʼязані з наявністю/відсутністю контакта та книгою вцілому - в класі AddressBook
4. Помилки, повʼязані з командами та параметрами від користувача - в хендлерах бота
5. Команди типу add мають виводити промпт у разі, якщо даний обʼєкт вже існує, і при згоді користувача - редагувати
6. ! Хендлери бота не працюють з класом Record, лише викликають відповідний метод класу AddressBook. Вся логіка для роботи з AddressBook знаходиться в самому класі та його методах
   
