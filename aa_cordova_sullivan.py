class Plant:
    def __init__(self, title, hp, power):
        self.name = title
        self.health = hp
        self.damage = power

    def attack(self, target_zombie):
        print(f"\n{self.name} strikes {target_zombie.name} dealing {self.damage} damage!")
        target_zombie.take_damage(self.damage)

    def take_damage(self, hit_points):
        self.health -= hit_points
        if self.health < 0:
            self.health = 0
        print(f"\n{self.name} took {hit_points} damage! Current Health: {self.health}")


class Zombie:
    def __init__(self, title, hp, power, gap):
        self.name = title
        self.health = hp
        self.damage = power
        self.distance = gap

    def move(self):
        if self.distance > 0:
            self.distance -= 1
        print(f"\n{self.name} advanced forward. Distance remaining: {self.distance}")

    def attack(self, target_plant):
        print(f"\n{self.name} strikes {target_plant.name} dealing {self.damage} damage!")
        target_plant.take_damage(self.damage)

    def take_damage(self, hit_points):
        self.health -= hit_points
        if self.health < 0:
            self.health = 0
        print(f"\n{self.name} took {hit_points} damage! (Current Health: {self.health})")


def run_game():
    first_plant = Plant("Repeater", 70, 20)
    second_plant = Plant("Threepeater", 80, 20)

    enemy = Zombie("Monster", 250, 30, 6)

    defenders = {first_plant, second_plant}

    round_num = 1

    while True:
        print(f"\nTurn {round_num}")

        for unit in defenders:
            if unit.health > 0:
                unit.attack(enemy)
            if enemy.health <= 0:
                print(f"\n{enemy.name} was defeated! The Plants secure the victory.")
                return

        if enemy.distance > 0:
            enemy.move()
        else:
            active_target = next((item for item in defenders if item.health > 0), None)
            if active_target:
                enemy.attack(active_target)

        if all(unit.health <= 0 for unit in defenders):
            print(f"All defending plants are destroyed! {enemy.name} WINS!")
            return

        print(f"\nEnd of Turn {round_num}")
        for unit in defenders:
            print(f"{unit.name} HP: {unit.health}")
        print(f"\n{enemy.name} HP: {enemy.health}")

        round_num += 1


if __name__ == "__main__":
    run_game()