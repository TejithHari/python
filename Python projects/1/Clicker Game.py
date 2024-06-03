import time
import json
import threading

class ClickerGame:
    def __init__(self):
        self.points = 0
        self.ppc = 1  # Points per click
        self.pps = 0  # Points per second
        self.upgrades = {
            'click_upgrade': {'cost': 10, 'ppc_increase': 1},
            'auto_clicker': {'cost': 50, 'pps_increase': 1}
        }
        self.load_game()

    def click(self):
        self.points += self.ppc
        print(f"Clicked! You have {self.points} points.")

    def buy_upgrade(self, upgrade_name):
        upgrade = self.upgrades[upgrade_name]
        if self.points >= upgrade['cost']:
            self.points -= upgrade['cost']
            if 'ppc_increase' in upgrade:
                self.ppc += upgrade['ppc_increase']
                print(f"PPC upgraded to {self.ppc}.")
            if 'pps_increase' in upgrade:
                self.pps += upgrade['pps_increase']
                print(f"PPS upgraded to {self.pps}.")
            upgrade['cost'] = int(upgrade['cost'] * 1.5)  # Increase cost for next purchase
        else:
            print("Not enough points to buy upgrade.")

    def display_stats(self):
        print(f"Points: {self.points}, PPC: {self.ppc}, PPS: {self.pps}")

    def save_game(self):
        with open('clicker_game_save.json', 'w') as file:
            json.dump({'points': self.points, 'ppc': self.ppc, 'pps': self.pps}, file)

    def load_game(self):
        try:
            with open('clicker_game_save.json', 'r') as file:
                data = json.load(file)
                self.points = data.get('points', 0)
                self.ppc = data.get('ppc', 1)
                self.pps = data.get('pps', 0)
        except FileNotFoundError:
            print("No save file found. Starting a new game.")

    def start_auto_clicker(self):
        def earn_points():
            while True:
                time.sleep(1)
                self.points += self.pps
        threading.Thread(target=earn_points, daemon=True).start()

def main():
    game = ClickerGame()
    game.start_auto_clicker()

    while True:
        print("\n1. Click\n2. Buy Click Upgrade (10 points)\n3. Buy Auto Clicker (50 points)\n4. Save\n5. Stats\n6. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            game.click()
        elif choice == '2':
            game.buy_upgrade('click_upgrade')
        elif choice == '3':
            game.buy_upgrade('auto_clicker')
        elif choice == '4':
            game.save_game()
            print("Game saved.")
        elif choice == '5':
            game.display_stats()
        elif choice == '6':
            game.save_game()
            print("Game saved. Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
