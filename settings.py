class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.alien_points = 50
        self.score_scale = 1.5
        self.framerate = 60

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 6
        self.bullet_speed_factor = 10
        self.bullet_horizontal_speed_factor = 7
        self.alien_speed_factor = 2.5
        self.fleet_direction = 1
        self.boost_speed_factor = 2
        self.last_boost = 0
        self.boost_hit = 0
        self.boost_time = 5.5
        self.boost_rarity = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
