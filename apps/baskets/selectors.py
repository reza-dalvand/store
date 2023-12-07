from apps.baskets.models import Basket, BasketDetail


def get_or_create_basket(user_id) -> Basket:
    basket, created = Basket.objects.prefetch_related("details").get_or_create(
        user_id=user_id, is_open=True
    )
    return basket


def change_or_add_product_in_user_basket(basket, product_id, product_count) -> bool:
    # if product is already existing in user basket
    product = basket.details.filter(product_id=product_id, basket_id=basket).first()
    if product:
        product.count += product_count
        product.save()
        return True

    # if not existing
    BasketDetail.objects.create(
        basket_id=basket.id, product_id=product_id, count=product_count
    )
    return False


def remove_product_in_user_basket(basket, product_id) -> bool:
    product = basket.details.filter(id=product_id).first()
    if product:
        product.delete()
        return True
    return False
