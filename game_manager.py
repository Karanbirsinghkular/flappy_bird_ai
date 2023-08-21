import random
import time

import pipe


class Game_manager:
    def __init__(self, bird_list, pipe_velx, pipe_dist_ll, pipe_dist_ul, pipe_color,
                 w, h, lower_space_limit, upper_space_limit, breadth_ll, breadth_ul):
        self.score = 0
        self.bird_list = bird_list
        self.pipe_velx = pipe_velx
        self.pipe_dist_ll = pipe_dist_ll
        self.pipe_dist_ul = pipe_dist_ul
        self.pipe_color = pipe_color
        self.pipelist_maxlen = 5
        self.pipelist = []
        self.w = w
        self.h = h
        self.lower_space_limit = lower_space_limit
        self.upper_space_limit = upper_space_limit
        self.breadth_ll = breadth_ll
        self.breadth_ul = breadth_ul
        rand = random.Random()
        space = rand.randint(lower_space_limit, upper_space_limit)
        self.pipelist.append(pipe.Pipe(w/2, rand.randint(50, h - space - 50), rand.randint(self.breadth_ll, self.breadth_ul), space, w, h, pipe_color))
        for i in range(self.pipelist_maxlen - 1):
            space = rand.randint(lower_space_limit, upper_space_limit)
            self.pipelist.append(
                pipe.Pipe(self.pipelist[i].posx + self.pipelist[i].breadth +
                          rand.randint(self.pipe_dist_ll, self.pipe_dist_ul), rand.randint(50, h - space - 50),
                          rand.randint(self.breadth_ll, self.breadth_ul), space, w, h,
                          pipe_color))
        self.dec = 0


    def addPipe(self):
        rand = random.Random()
        space = rand.randint(self.lower_space_limit, self.upper_space_limit) - self.dec
        self.dec += 0
        self.pipelist.append(pipe.Pipe(self.pipelist[len(self.pipelist) - 1].posx + self.pipelist[len(self.pipelist) - 1].breadth + rand.randint(self.pipe_dist_ll, self.pipe_dist_ul), rand.randint(50, self.h - space - 50), rand.randint(self.breadth_ll, self.breadth_ul), space, self.w, self.h,
                          self.pipe_color))

    def removePipe(self, pipe):
        for bird in self.bird_list:
            yscore = 1 / max(2, abs(pipe.l1 + (pipe.space / 2) - bird.posy))
            self.updatescore(bird, pipe, 1 + yscore)
            bird.pipe1 = False
        self.pipelist.remove(pipe)

    def update(self, dt):
        for bird in self.bird_list:
            pipe = self.pipelist[0]
            if bird.pipe1:
                yscore = 1 / max(2, abs(pipe.l1 + pipe.space / 2 - bird.posy))
                bird.setAlive(self.isAlive(bird), yscore)#yscore
            else:
                bird.setAlive(self.isAlive(bird), 0)
            if not bird.getAlive():
                bird.applyForce(0.025)
                bird.update(dt)
            bird.update(dt)
        var = False
        for bird in self.bird_list:
            var = var or bird.getAlive()
        if not var:
            return
        for each in self.pipelist:
            each.update(self.pipe_velx, dt)
            if not each.checkinbounds():
                self.removePipe(self.pipelist[0])
                self.addPipe()

    def birdjump(self, forcey, angvel):
        for bird in self.bird_list:
            bird.jump(forcey, angvel)

    def show(self, screen, val):

        if val:
            self.bird_list[-1].show(screen)
            if self.bird_list[-1].alive:
                for each in self.pipelist:
                    each.show(screen)
            time.sleep(0.003)
        else:
            for bird in self.bird_list:
                bird.show(screen)
            for each in self.pipelist:
                each.show(screen)

    def isAlive(self, bird):
        if bird.checkinbounds():
            for each in self.pipelist:
                if each.checkinpipe(bird):
                    return False
            return True

    def updatescore(self, bird, pipe, val):
        if (bird.posx > pipe.posx + pipe.breadth):
            bird.incrementscore(val)
        self.score = max(self.score, bird.score)

    def getnextpipe(self, bird):
        for pipe in self.pipelist:
            if (bird.posx < pipe.posx + pipe.breadth):
                return pipe

