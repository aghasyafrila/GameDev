 #untuk menghitung pergerakan kamera, gambar, aktor/karakter dan durasi
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase 
from direct.task import Task 
from direct.actor.Actor import Actor 
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3 


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        # memuat environment pada model
        self.scene = self.loader.loadModel("models/environment")
        # Mengatur ulang model yang akan dirender
        self.scene.reparentTo(self.render)
        # Menerapkan transformasi skala dan posisi pada model
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Menambahkan perintah spinCameraTask ke pengelola tugas
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load dan mengubah aktor
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop animasi
        self.pandaActor.loop("walk")

        # Membuat interval lerp yang berguna untuk membuat karakter berjalan bolak-balik
        posInterval1 = self.pandaActor.posInterval(13,
                                                   Point3(0, -10, 0),
                                                   startPos=Point3(0, 10, 0))
        posInterval2 = self.pandaActor.posInterval(13,
                                                   Point3(0, 10, 0),
                                                   startPos=Point3(0, -10, 0))
        hprInterval1 = self.pandaActor.hprInterval(3,
                                                   Point3(180, 0, 0),
                                                   startHpr=Point3(0, 0, 0))
        hprInterval2 = self.pandaActor.hprInterval(3,
                                                   Point3(0, 0, 0),
                                                   startHpr=Point3(180, 0, 0))

        # Memuat urutan yang mengoordinasikan interval
        self.pandaPace = Sequence(posInterval1, hprInterval1,
                                  posInterval2, hprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Tentukan aturan untuk menggerakkan kamera
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

#inisialisasi Function MyApp() ke variabel app
app = MyApp()
mySound = app.loader.loadSfx("music/musicbox.ogg")
#musik diputar
mySound.play()
#untuk mengulang musik
mySound.setLoop(True)
#mengatur volume
mySound.setVolume(10)
#untuk menjalankan aplikasi
app.run()
