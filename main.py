from vkinder_bot import bot


if __name__ == '__main__':
    with open('tokens.ini', 'r', encoding='utf-8') as file:
        user_token, public_token = file.readlines()
    bot(user_token=user_token, public_token=public_token,
        db_user_name='postgres', db_password='your pass', db='your db',
        memory_days=5)
