def  pizza_type(type="Mix veggi"):
    """Return the type of pizza"""
    return type

print(pizza_type.__doc__)
print(pizza_type.__name__)

def generate_bill(pizza=0, burger=0):
    """
    Calculate the bill of pizza and burger

    :param pizza: Number of pizza(200rupees each)
    :param burger: Number of burger (60 rupess each)
    :return: (total amount, thank you for choosing our cafe0)

    """
    total = pizza*200 + burger*60
    return total, "Thank you for visiting us"