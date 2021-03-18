from services import pipocoin_util
from services import pipocoin_messages as messages
from models import pipocoin_dao


def create(origin_id, command_stack):
    try:
        if pipocoin_util.does_user_exists_by_id(origin_id):
            return messages.create.fail_already_registered_user()

        user_name = command_stack[0]
        created_user = pipocoin_dao.create_new_user(
            origin_id,
            user_name
        )

        return messages.create.success_user_created(created_user)
    except Exception as e:
        print(e)
        return messages.default.fail_error_occurred()


def delete(origin_id, command_stack):
    try:
        if not pipocoin_util.does_user_exists_by_id(origin_id):
            return messages.delete.fail_not_registered_user()

        deleted_user_id = pipocoin_dao.delete_user(
            origin_id
        )

        return messages.delete.success_user_deleted(deleted_user_id)
    except Exception as e:
        print(e)
        return messages.default.fail_error_occurred()


def transfer(origin_id, command_stack):
    try:
        from_twitter_id = origin_id
        amount = command_stack[0]
        to_user_name = command_stack[1]

        if not pipocoin_util.does_user_exists_by_id(from_twitter_id):
            return messages.transfer.fail_not_registered_user()
        if not pipocoin_util.does_user_exists_by_name(to_user_name):
            return messages.transfer.fail_not_registered_target_user()
        if not pipocoin_util.user_has_enough_money(from_twitter_id, amount):
            return messages.transfer.fail_not_enough_money_to_tranfer()

        pipocoin_dao.transfer_to_user(
            from_twitter_id,
            to_user_name,
            amount
        )

        return messages.transfer.success_tranferred(from_twitter_id, to_user_name, amount)
    except Exception as e:
        print(e)
        return messages.default.fail_error_occurred()


def work(origin_id, command_stack):
    try:
        if not pipocoin_util.does_user_exists_by_id(origin_id):
            return messages.work.fail_not_registered_user()

        AMOUNT = 10.0
        user = pipocoin_dao.add_money_to_user(
            origin_id,
            AMOUNT
        )

        return messages.work.success_worked(user, AMOUNT)
    except Exception as e:
        print(e)
        return messages.default.fail_error_occurred()


command_list = {
    "create": create,
    "criar": create,
    "delete": delete,
    "deletar": delete,
    "transfer": transfer,
    "transferir": transfer,
    "work": work,
    "trabalhar": work,
}
