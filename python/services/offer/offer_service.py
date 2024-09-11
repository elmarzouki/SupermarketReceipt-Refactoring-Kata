from models.discount import Discount
from models.offer import Offer, SpecialOfferType
from models.product import Product
from services.offer.offer_strategy import (FiveForAmountOffer, TenPercentOffer,
                                           ThreeForTwoOffer, TwoForAmountOffer)


class OfferService:
    def __init__(self):
        self._strategies = {
            SpecialOfferType.THREE_FOR_TWO: ThreeForTwoOffer(),
            SpecialOfferType.TWO_FOR_AMOUNT: TwoForAmountOffer(),
            SpecialOfferType.FIVE_FOR_AMOUNT: FiveForAmountOffer(),
            SpecialOfferType.TEN_PERCENT_DISCOUNT: TenPercentOffer(),
        }

    def apply_offer(
        self, offer: Offer, product: Product, quantity: int, unit_price: int
    ) -> Discount:
        strategy = self._strategies.get(offer.offer_type)
        if strategy:
            return strategy.calculate_discount(product, quantity, unit_price, offer)
        return None
