class Constants:
    ACTIVE = 1
    INACTIVE = 0
    INPUT_DEVICE = 1
    OUTPUT_DEVICE = 2
    IN_OUTPUT_DEVICE = 3
    GAME_STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    DEVICE_TYPE = (
        (INPUT_DEVICE, 'Input'),
        (INPUT_DEVICE, 'Output'),
        (IN_OUTPUT_DEVICE, 'Input/Output'),
    )