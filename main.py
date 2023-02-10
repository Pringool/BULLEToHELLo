import turtle
from config import *
from letters import Letters
import time
from database import *
import customtkinter as ctk



class Leaderboard(ctk.CTk):
    def __init__(self, database:Database) -> None:
        super().__init__()
        self.db = database
        self.geometry("800x600")
        self.title("Leaderboard")
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20,padx=20, fill="both", expand=True)
        self.leaderboard_text = ctk.CTkTextbox(self.frame, width=700, height=550)
        self.leaderboard_text.pack()
        self.insert_index=0
        
    def get_data_from_database(self):
        self.data = self.db.read_data()
        print("Score board")

    
    def show_leaderboard(self):
        self.get_data_from_database()
        for i in self.data:
            player = '                   '.join(map(str, i))
            self.leaderboard_text.insert(f"{self.insert_index}.0",player+"\n")

class Player:
    def __init__(self, t:turtle.Turtle) -> None:
        self.turtle = t
        self.turtle.color("white")
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.speed:float = 4

        
        b1,b2,b3 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
        b1.color(PLAYER_SHOT_COLOR)
        b2.color(PLAYER_SHOT_COLOR)
        b3.color(PLAYER_SHOT_COLOR)
        b1.left(90)
        b2.left(90)
        b3.left(90)
        b1.pu()
        b2.pu()
        b3.pu()
        b1.ht()
        b2.ht()
        b3.ht()
        b1.shape("arrow")
        b2.shape("arrow")
        b3.shape("arrow")
        self.bullets = [b1,b2,b3]
        self.shots = []
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        self.turtle.goto(self.x,self.y)
            
        for shot in self.shots:
            if shot.ycor() < YMAX:
                shot.fd(7)
            else:
                shot.ht()
                self.shots.remove(shot)
                
                
        
    def shoot(self):
        if len(self.shots) < len(self.bullets):
            shot_times = 0
            for bullet in self.bullets:
                if bullet not in self.shots:
                    if shot_times < 1: 
                        shot_times += 1
                        bullet.setpos(self.turtle.xcor(),self.turtle.ycor())
                        bullet.st()
                        self.shots.append(bullet)
        
    def start_left(self):
        self.dx = -self.speed
    
    def start_right(self):
        self.dx = self.speed

    def stop_left(self):
        self.dx = 0

    def stop_right(self):
        self.dx = 0

    def start_up(self):
        self.dy = self.speed

    def start_down(self):
        self.dy = -self.speed

    def stop_up(self):
        self.dy = 0

    def stop_down(self):
        self.dy = 0
        
class Enemy:
    def __init__(self, t:turtle.Turtle, x:float, y:float, health:int, player:turtle.Turtle) -> None:
        self.turtle = t
        self.turtle.setpos((x,y))
        self.turtle.shape("square")
        self.turtle.turtlesize(2,2)
        self.turtle.color((1,0.4,0.2))
        self.health = health
        self.turtle.st()
        self.is_dead = False
    
        self.x = x
        self.y = y
        self.dx = random.uniform(1,3)
        self.dy = random.uniform(1,3)
    
        b1,b2,b3,b4,b5,b6,b7,b8,b9,bb1= turtle.Turtle(), turtle.Turtle(),turtle.Turtle(), turtle.Turtle(),turtle.Turtle(), turtle.Turtle(),turtle.Turtle(), turtle.Turtle(),turtle.Turtle(), turtle.Turtle()
        b1.color(ENEMY_SHOT_COLOR)
        b2.color(ENEMY_SHOT_COLOR)
        b1.pu()
        b2.pu()
        b1.ht()
        b2.ht()
        b1.shape("arrow")
        b2.shape("arrow")
        
        b3.color(ENEMY_SHOT_COLOR)
        b4.color(ENEMY_SHOT_COLOR)
        b3.pu()
        b4.pu()
        b3.ht()
        b4.ht()
        b3.shape("arrow")
        b4.shape("arrow")
        
        b5.color(ENEMY_SHOT_COLOR)
        b6.color(ENEMY_SHOT_COLOR)
        b5.pu()
        b6.pu()
        b5.ht()
        b6.ht()
        b5.shape("arrow")
        b6.shape("arrow")
        
        b7.color(ENEMY_SHOT_COLOR)
        b8.color(ENEMY_SHOT_COLOR)
        b7.pu()
        b8.pu()
        b7.ht()
        b8.ht()
        b7.shape("arrow")
        b8.shape("arrow")
        
        b9.color(ENEMY_SHOT_COLOR)
        bb1.color(ENEMY_SHOT_COLOR)
        b9.pu()
        bb1.pu()
        b9.ht()
        bb1.ht()
        b9.shape("arrow")
        bb1.shape("arrow")
        
        self.bullets = [b1,b2,b3,b4,b5,b6,b7,b8,b9,bb1]
        self.shots = []

        self.player_turtle = player
        self.start_time_enemy_shot_delay = time.time()
    def attack(self):
        if len(self.shots) < len(self.bullets):
            shot_times = 0
            for i in range(0, len(self.bullets)):
                for bullet in self.bullets:
                    if bullet not in self.shots:
                        if shot_times < 1: 
                            shot_times += 1
                            bullet.setpos(self.turtle.xcor(),self.turtle.ycor())
                            bullet.setheading(bullet.towards(self.player_turtle.xcor()*random.randint(-2,2), self.player_turtle.ycor()*random.randint(-2,2)))
                            bullet.st()
                            self.shots.append(bullet)

    
    def update(self):
        if self.x > XMAX or self.x < XMIN:
            self.dx *= -1
        if self.y > YMAX or self.y < YMIN:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy
        self.turtle.setheading(self.turtle.towards(self.player_turtle.xcor(), self.player_turtle.ycor()))
        self.turtle.goto(self.x,self.y)
        end_time = time.time()
        if end_time-self.start_time_enemy_shot_delay >= ENEMY_SHOT_DELAY:
            self.start_time_enemy_shot_delay = end_time
            self.attack()
    
        for shot in self.shots:
            if shot.xcor() > XMAX or shot.xcor() < XMIN or shot.ycor() > YMAX or shot.ycor() < YMIN:
                shot.ht()
                self.shots.remove(shot)   
            else:
                shot.fd(7)
    
    def take_damage(self):
        self.health-=1
        if self.health <= 0:
            self.turtle.ht()
            self.is_dead = True
            for shot in self.shots:
                shot.ht()
     
class Game:
    def __init__(self) -> None:
        #self.player_name = input("Whats your name?: ")
        self.player_name = window.textinput("What's your name?", " ")
        if self.player_name is None:
            print("Goodbye!")
            window.clear()
            window.bye()
        window.tracer(1)
        self.letter_turtle = turtle.Turtle()
        self.letter_turtle.hideturtle()
        self.lt = Letters(self.letter_turtle)
        self.lt.print_text("Game Start/Press space", "white")
        window.tracer(0)
        self.game_pressed = False
        self.score = 0
        self.game_ended = False
        
        self.enemy_health = 3
        self.enemies = []
        self.enemy1 = turtle.Turtle()
        self.enemy1.pu()
        
        self.enemy2 = turtle.Turtle()
        self.enemy2.pu()
        self.enemy2.ht()
        
        self.enemy3 = turtle.Turtle()
        self.enemy3.pu()
        self.enemy3.ht()
        
        self.enemy4 = turtle.Turtle()
        self.enemy4.pu()
        self.enemy4.ht()
        
        self.enemy5 = turtle.Turtle()
        self.enemy5.pu()
        self.enemy5.ht()
        
        self.enemy6 = turtle.Turtle()
        self.enemy6.pu()
        self.enemy6.ht()
        
        self.enemy7 = turtle.Turtle()
        self.enemy7.pu()
        self.enemy7.ht()
        
        self.enemy8 = turtle.Turtle()
        self.enemy8.pu()
        self.enemy8.ht()
        
        self.enemy9 = turtle.Turtle()
        self.enemy9.pu()
        self.enemy9.ht()
        
        self.enemy10 = turtle.Turtle()
        self.enemy10.pu()
        self.enemy10.ht()
        
        self.enemy11 = turtle.Turtle()
        self.enemy11.pu()
        self.enemy11.ht()
        
        
        
        self.all_enemies = [self.enemy1, self.enemy2, self.enemy3, self.enemy4, self.enemy5, self.enemy6, self.enemy7, self.enemy8, self.enemy9, self.enemy10, self.enemy11]
        
        self.waves ={
            'wave1': 1,
            'wave2': 2,
            'wave3': 2,
            'wave4': 4,
            'wave5': 5,
            'wave6': 5,
            'wave7': 5,
            'wave8': 5,
            'wave9': 5,
            'wave10': 5,
            'wave11': 5,
            'wave12': 5,
            'wave13': 5,
            'wave14': 5,
            'wave15': 6,
            'wave16': 7,
            'wave17': 7,
            'wave18': 7,
            'wave19': 7,
            'wave20': 7,
            'wave21': 7,
            'wave22': 7,
            'wave23': 7,
            'wave24': 7,
            'wave25': 7,
            'wave26': 7,
            'wave27': 8,
            'wave28': 9,
            'wave29': 9,
            'wave30': 9,
            'wave31': 9,
            'wave32': 9,
            'wave33': 5,
            'wave34': 5,
            'wave35': 10,
            'wave36': 3,
            'wave37': 3,
            'wave38': 3,
            'wave39': 3,
            'wave40': 2,
            'wave40': 2,
            'wave40': 2,
            'wave40': 2,
            'wave41': 11
        }
        
        self.wave_index = 0
        all_waves = list(self.waves.items())
        self.current_wave = all_waves[self.wave_index]
        
        self.db = Database()
        
    def start(self):
        player_turtle = turtle.Turtle("square")
        player_turtle.penup()
        player_turtle.hideturtle()
        self.player = Player(player_turtle)
        
        window.onkeypress(self.player.start_up,'w')
        window.onkeypress(self.player.start_left,'a')
        window.onkeypress(self.player.start_right,'d')
        window.onkeypress(self.player.start_down,'s')
        
        window.onkey(self.player.shoot, "l")
        
        window.onkeyrelease(self.player.stop_up,'w')
        window.onkeyrelease(self.player.stop_left,'a')
        window.onkeyrelease(self.player.stop_right,'d')
        window.onkeyrelease(self.player.stop_down,'s')
        
        window.onkey(self.game_press, 'space')
        window.onkey(self.game_over, "g")
        window.listen()
        
        self.game_start = time.time()
        self.game_start_time_format = time.strftime("%H:%M:%S", time.localtime())
        self.__game()
        
        
    def wave(self):
        if len(self.enemies) == 0:
            self.enemy_health+=1
            self.get_current_wave()
            self.lt.print_text(f"Next WAVE:/{self.current_wave[0]}", "white")
            window.ontimer(self.letter_turtle.clear, WAVE_DELAY)
            self.spawn_enemy(self.current_wave[1])
            
            
    def get_current_wave(self):
        self.wave_index += 1
        all_waves = list(self.waves.items())
        if self.wave_index < len(self.waves):
            self.current_wave = all_waves[self.wave_index]
            print(self.current_wave[0])
        else:
            self.game_won()
     
    def spawn_enemy(self, amount:int):
        for i in range(0, amount):
            self.all_enemies[i].st()
            self.enemies.append(Enemy(self.all_enemies[i], random.randint(0, 200), random.randint(100,300),self.enemy_health, self.player.turtle))
    
    def game_press(self):
        self.game_pressed = True
    
    def __game(self):
        reset_value = 0
        while True:
            if not self.game_ended:
                if self.game_pressed:
                    if reset_value == 0:
                        reset_value += 1
                        self.letter_turtle.clear()
                        self.player.turtle.showturtle()
                        self.enemies.append(Enemy(self.enemy1, 100, 200,self.enemy_health, self.player.turtle))
                        
                    window.ontimer(self.update(),TIMER)
                
            window.update()
    
    def update(self):
        collision_enemy:Enemy = self.check_collision_enemy_shot()
        if collision_enemy != None:
            collision_enemy.take_damage()
            self.score+=1
            if collision_enemy.is_dead:
                self.enemies.remove(collision_enemy)
                self.wave()
        self.check_collision_player_enemy()
        self.player.update()
        self.check_collision_player_shot()
        for enemy in self.enemies:
            enemy.update()
        
    def check_collision_enemy_shot(self):
        for a in self.player.shots:
            for b in self.enemies:
                if abs(a.xcor() - b.turtle.xcor()) < 25 and abs(a.ycor() - b.turtle.ycor()) < 25:
                    print("Hit")
                    self.score += 1
                    a.ht()
                    self.player.shots.remove(a)
                        
                    return b
        return None
                
    def check_collision_player_shot(self):
        for enemy in self.enemies:
            for shot in enemy.shots:
                if abs(self.player.turtle.xcor() - shot.xcor()) < 25 and abs(self.player.turtle.ycor() - shot.ycor()) < 25:
                    print("Player Hit")
                    self.game_over()
                    
    def check_collision_player_enemy(self):
        for b in self.enemies:
            if abs(self.player.turtle.xcor() - b.turtle.xcor()) < 50 and abs(self.player.turtle.ycor() - b.turtle.ycor()) < 50:
                self.game_over()
        
    def game_over(self):
        if not self.game_ended:
            self.letter_turtle.clear()
            self.end_time = time.time()
            self.game_end_time_format = time.strftime("%H:%M:%S", time.localtime())
            self.end_time
            self.game_ended = True
            self.lt.print_text(f"Game OVER/Score {str(self.score)}", "white")
            self.player.turtle.ht()
            for enemy in self.enemies:
                enemy.turtle.ht()
                self.enemies.remove(enemy)
            time_for_game = self.end_time - self.game_start
            self.db.add_to_database(self.current_wave[0], self.score, self.player_name, self.game_start_time_format, self.game_end_time_format, time_for_game)  
            Leaderboard(self.db).show_leaderboard()
        
    def game_won(self):
        if not self.game_ended:
            self.letter_turtle.clear()
            self.end_time = time.time()
            self.game_end_time_format = time.strftime("%H:%M:%S", time.localtime())
            self.game_ended = True
            self.lt.print_text(f"Game WON/Score {str(self.score)}", "white")
            self.player.turtle.ht()
            for enemy in self.enemies:
                enemy.turtle.ht()
                self.enemies.remove(enemy)
            time_for_game = self.end_time - self.game_start
            self.db.add_to_database(self.current_wave[0], self.score, self.player_name, self.game_start_time_format, self.game_end_time_format, time_for_game)   
            Leaderboard(self.db).show_leaderboard()
            
if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.title(GAME_NAME)
    window.tracer(0)
    window.bgcolor("black")
    try:
        game = Game()
        game.start()
    except Exception as e:
        print(e)