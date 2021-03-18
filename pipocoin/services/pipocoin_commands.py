from services import pipocoin_util
import services.pipocoin_messages as messages
from models import user_DAO
from models.user_model import User


def create(origin_id, command_stack):
    try:
        user = User(user_id=origin_id, user_name=command_stack[0])

        if pipocoin_util.does_user_exists_by_id(user):
            return messages.create.fail_already_registered_user()

        created_user = user_DAO.create_new_user(
            user
        )

        return messages.create.success_user_created(created_user)
    except Exception as e:
        print(e)
        return messages.create.fail_error_occurred()


def delete(origin_id, command_stack):
    try:
        user = User(user_id=origin_id)

        if not pipocoin_util.does_user_exists_by_id(user):
            return messages.delete.fail_not_registered_user()

        user_DAO.delete_user(
            user
        )

        return messages.delete.success_user_deleted(user)
    except Exception as e:
        print(e)
        return messages.default.fail_error_occurred()


def transfer(origin_id, command_stack):
    try:
        from_user = User(user_id=origin_id)
        to_user = User(user_name=command_stack[1])
        amount = round(float(command_stack[0]), 2)

        if not pipocoin_util.does_user_exists_by_id(from_user):
            return messages.transfer.fail_not_registered_user()
        if not pipocoin_util.does_user_exists_by_name(to_user):
            return messages.transfer.fail_not_registered_target_user()
        if not pipocoin_util.user_has_enough_money_by_id(from_user, amount):
            return messages.transfer.fail_not_enough_money_to_tranfer()

        user_DAO.transfer_to_user(
            from_user,
            to_user,
            amount
        )

        return messages.transfer.success_tranferred(from_user, to_user, amount)
    except Exception as e:
        print(e)
        return messages.transfer.fail_error_occurred()


def work(origin_id, command_stack):
    try:
        user_worker = User(user_id=origin_id)

        if not pipocoin_util.does_user_exists_by_id(user_worker):
            return messages.work.fail_not_registered_user()

        AMOUNT = 9.99
        user = user_DAO.add_money_to_user(
            user_worker,
            AMOUNT
        )

        return messages.work.success_worked(user, AMOUNT)
    except Exception as e:
        print(e)
        return messages.work.fail_error_occurred()


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
