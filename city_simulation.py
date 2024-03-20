import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (200, 200, 200)
HOUSE_COLOR = (0, 128, 0)
COMMERCIAL_COLOR = (0, 0, 255)
INDUSTRIAL_COLOR = (255, 255, 0)
ROAD_COLOR = (169, 169, 169)
ROAD_MARKING_COLOR = (255, 255, 0)
CROSSROAD_COLOR = (255, 0, 0)
BULLDOZER_COLOR = (255, 0, 0)
ZONE_SIZE = 20

class CitySimulation:
    def __init__(self):
        pygame.init()  # Initialisiere Pygame
        pygame.font.init()  # Initialisiere die Schriftartenbibliothek
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("City Simulation")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.house_zones = []
        self.commercial_zones = []
        self.industrial_zones = []
        self.road_segments = []
        self.selected_zone = None
        self.building_in_progress = False
        self.residential_demand = 0
        self.commercial_demand = 0
        self.industrial_demand = 0
        self.residential_zones_happiness = []
        self.residential_zones_unemployment = []
        self.commercial_zones_happiness = []
        self.industrial_zones_happiness = []
        self.environmental_impact = 0

        # Buttons für Zonen und Bulldozer
        self.house_button = pygame.Rect(10, SCREEN_HEIGHT - 50, 30, 30)
        self.commercial_button = pygame.Rect(50, SCREEN_HEIGHT - 50, 30, 30)
        self.industrial_button = pygame.Rect(90, SCREEN_HEIGHT - 50, 30, 30)
        self.road_button = pygame.Rect(130, SCREEN_HEIGHT - 50, 30, 30)
        self.bulldozer_button = pygame.Rect(170, SCREEN_HEIGHT - 50, 30, 30)

        # Button für Statistik-Untermenü
        self.stats_menu_button = pygame.Rect(10, 10, 30, 30)
        self.stats_menu_open = False
        self.stats_menu_buttons = [
            pygame.Rect(50, 10, 150, 30),  # Button für Arbeitslosigkeit
            pygame.Rect(50, 50, 150, 30),  # Button für Zufriedenheit
            pygame.Rect(50, 90, 150, 30),  # Button für Umweltauswirkungen
        ]

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 or event.button == 5:
                    continue
                if self.house_button.collidepoint(event.pos):
                    self.selected_zone = "house"
                    self.building_in_progress = False
                elif self.commercial_button.collidepoint(event.pos):
                    self.selected_zone = "commercial"
                    self.building_in_progress = False
                elif self.industrial_button.collidepoint(event.pos):
                    self.selected_zone = "industrial"
                    self.building_in_progress = False
                elif self.road_button.collidepoint(event.pos):
                    self.selected_zone = "road"
                    self.building_in_progress = False
                elif self.bulldozer_button.collidepoint(event.pos):
                    self.selected_zone = "bulldozer"
                    self.building_in_progress = False
                elif self.stats_menu_button.collidepoint(event.pos):
                    self.stats_menu_open = not self.stats_menu_open
                elif self.stats_menu_open:
                    for button in self.stats_menu_buttons:
                        if button.collidepoint(event.pos):
                            self.handle_stats_button_click(self.stats_menu_buttons.index(button))
            elif event.type == pygame.MOUSEMOTION and self.building_in_progress:
                self.add_zone(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.building_in_progress = False

    def update(self):
        self.update_residential_demand()
        self.update_commercial_demand()
        self.update_industrial_demand()
        self.update_happiness()
        self.update_unemployment()
        self.update_environmental_impact()

    def update_residential_demand(self):
        population = len(self.house_zones)
        self.residential_demand = max(0, population - len(self.house_zones))

    def update_commercial_demand(self):
        self.commercial_demand = len(self.house_zones) // 5

    def update_industrial_demand(self):
        self.industrial_demand = len(self.house_zones) // 10

    def update_happiness(self):
        self.update_residential_happiness()
        self.update_commercial_happiness()
        self.update_industrial_happiness()

    def update_residential_happiness(self):
        self.residential_zones_happiness = []
        for zone in self.house_zones:
            happiness = random.uniform(0.5, 1.0)
            for commercial_zone in self.commercial_zones:
                if zone.colliderect(commercial_zone):
                    happiness += 0.1
            self.residential_zones_happiness.append(happiness)

    def update_commercial_happiness(self):
        self.commercial_zones_happiness = []
        for zone in self.commercial_zones:
            happiness = random.uniform(0.5, 1.0)
            for residential_zone in self.house_zones:
                if zone.colliderect(residential_zone):
                    happiness += 0.1
            self.commercial_zones_happiness.append(happiness)

    def update_industrial_happiness(self):
        self.industrial_zones_happiness = []
        for zone in self.industrial_zones:
            happiness = random.uniform(0.5, 1.0)
            self.industrial_zones_happiness.append(happiness)

    def update_unemployment(self):
        for zone in self.house_zones:
            unemployment = random.uniform(0, 0.5)
            for industrial_zone in self.industrial_zones:
                if zone.colliderect(industrial_zone):
                    unemployment += 0.2
            self.residential_zones_unemployment.append(unemployment)

    def update_environmental_impact(self):
        self.environmental_impact = len(self.industrial_zones) * 0.1

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)

        for x in range(0, SCREEN_WIDTH, ZONE_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, ZONE_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        self.draw_zones(self.house_zones, HOUSE_COLOR)
        self.draw_zones(self.commercial_zones, COMMERCIAL_COLOR)
        self.draw_zones(self.industrial_zones, INDUSTRIAL_COLOR)

        for segment in self.road_segments:
            pygame.draw.line(self.screen, ROAD_COLOR, segment[0], segment[1], 5)
            self.draw_road_markings(segment[0], segment[1])

        pygame.draw.rect(self.screen, BULLDOZER_COLOR, self.bulldozer_button)

        self.draw_zone_button(self.house_button, HOUSE_COLOR)
        self.draw_zone_button(self.commercial_button, COMMERCIAL_COLOR)
        self.draw_zone_button(self.industrial_button, INDUSTRIAL_COLOR)
        self.draw_zone_button(self.road_button, ROAD_COLOR)

        pygame.draw.rect(self.screen, (100, 100, 100), self.stats_menu_button)
        pygame.draw.polygon(self.screen, (255, 255, 255), [(20, 20), (20, 30), (30, 25)])

        if self.stats_menu_open:
            pygame.draw.rect(self.screen, (150, 150, 150), (0, 0, 200, 150))
            for button in self.stats_menu_buttons:
                pygame.draw.rect(self.screen, (100, 100, 100), button)
            font = pygame.font.Font(None, 24)
            texts = ["Unemployment", "Happiness", "Environmental Impact"]
            for i, text in enumerate(texts):
                label = font.render(text, True, (255, 255, 255))
                self.screen.blit(label, (60, 15 + 40 * i))

        self.draw_unemployment_text()
        self.draw_happiness_text()
        self.draw_environmental_impact_text()

        pygame.display.flip()

    def draw_zone_button(self, button_rect, color):
        pygame.draw.rect(self.screen, color, button_rect)

    def draw_zones(self, zones, color):
        for zone in zones:
            pygame.draw.rect(self.screen, color, zone)

    def draw_road_markings(self, start, end):
        unit_vector = ((end[0] - start[0]) / ZONE_SIZE, (end[1] - start[1]) / ZONE_SIZE)
        for i in range(1, ZONE_SIZE):
            mark_start = (start[0] + unit_vector[0] * i, start[1] + unit_vector[1] * i)
            mark_end = (mark_start[0] + unit_vector[0] * 10, mark_start[1] + unit_vector[1] * 10)
            pygame.draw.line(self.screen, ROAD_MARKING_COLOR, mark_start, mark_end, 2)

    def draw_unemployment_text(self):
        if not self.stats_menu_open:
            return
        font = pygame.font.Font(None, 24)
        average_unemployment = sum(self.residential_zones_unemployment) / max(1, len(self.residential_zones_unemployment))
        text = font.render(f"Average Unemployment: {average_unemployment:.2f}", True, (0, 0, 0))
        self.screen.blit(text, (10, 100))

    def draw_happiness_text(self):
        if not self.stats_menu_open:
            return
        font = pygame.font.Font(None, 24)
        average_residential_happiness = sum(self.residential_zones_happiness) / max(1, len(self.residential_zones_happiness))
        average_commercial_happiness = sum(self.commercial_zones_happiness) / max(1, len(self.commercial_zones_happiness))
        average_industrial_happiness = sum(self.industrial_zones_happiness) / max(1, len(self.industrial_zones_happiness))
        text = font.render(
            f"Average Happiness - Residential: {average_residential_happiness:.2f} | Commercial: {average_commercial_happiness:.2f} | Industrial: {average_industrial_happiness:.2f}",
            True, (0, 0, 0))
        self.screen.blit(text, (10, 130))

    def draw_environmental_impact_text(self):
        if not self.stats_menu_open:
            return
        font = pygame.font.Font(None, 24)
        text = font.render(f"Environmental Impact: {self.environmental_impact:.2f}", True, (0, 0, 0))
        self.screen.blit(text, (10, 160))

    def handle_stats_button_click(self, button_index):
        if button_index == 0:
            print("Unemployment Button Clicked")
        elif button_index == 1:
            print("Happiness Button Clicked")
        elif button_index == 2:
            print("Environmental Impact Button Clicked")

if __name__ == "__main__":
    simulation = CitySimulation()
    simulation.run()
    pygame.quit()
    sys.exit()
