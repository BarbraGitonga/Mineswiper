import settings as st

def height_prct(percentage):
    """height percentage

    Args:
        percentage (integer): percentage height to be used

    Returns:
        integer: value of percentage of height
    """
    return (st.HEIGHT / 100) * percentage

def width_prct(percentage):
    """_summary_

    Args:
        percentage (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (st.WIDTH / 100) * percentage
