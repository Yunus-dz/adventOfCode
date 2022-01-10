EXPECTED_BAKE_TIME = 40
PREP_PER_LAYER_MINS = 2

def bake_time_remaining(elapsed_bake_time):
    """Trivial"""

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(num_layers):
    """Trivial"""
    return num_layers * PREP_PER_LAYER_MINS


def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    """Trivial"""
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time

    
