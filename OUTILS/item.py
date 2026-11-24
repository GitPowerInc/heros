items = {
    "potion": {
        "common": {"health": 20, "mana": 0, "price": 10},
        "rare":   {"health": 50, "mana": 10, "price": 40},
        "epic":   {"health": 100, "mana": 30, "price": 100},
    },
    "sword": {
        "common": {"damage": 5, "price": 15},
        "rare":   {"damage": 12, "price": 60},
        "epic":   {"damage": 25, "price": 150},
    },
}

common_potion_health = items["potion"]["common"]["health"]
print(common_potion_health)  # 20