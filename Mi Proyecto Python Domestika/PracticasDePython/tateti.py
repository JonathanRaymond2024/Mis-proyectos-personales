
import tkinter as tk
from tkinter import messagebox

class TaTeTi:
    def __init__(self, root):
        self.root = root
        self.root.title("Ta Te Ti")

        self.jugador = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]

        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                  command=lambda f=fila, c=col: self.jugar(f, c))
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def jugar(self, fila, col):
        if self.tablero[fila][col] == "":
            self.tablero[fila][col] = self.jugador
            self.botones[fila][col].config(text=self.jugador, state="disabled")

            if self.hay_ganador(self.jugador):
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.jugador} ha ganado!")
                self.resetear_tablero()
            elif self.tablero_lleno():
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.resetear_tablero()
            else:
                self.jugador = "O" if self.jugador == "X" else "X"

    def hay_ganador(self, jugador):
        for i in range(3):
            if all([self.tablero[i][j] == jugador for j in range(3)]) or \
               all([self.tablero[j][i] == jugador for j in range(3)]):
                return True

        if all([self.tablero[i][i] == jugador for i in range(3)]) or \
           all([self.tablero[i][2 - i] == jugador for i in range(3)]):
            return True

        return False

    def tablero_lleno(self):
        return all(self.tablero[f][c] != "" for f in range(3) for c in range(3))

    def resetear_tablero(self):
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for fila in range(3):
            for col in range(3):
                self.botones[fila][col].config(text="", state="normal")
        self.jugador = "X"

if __name__ == "__main__":
    root = tk.Tk()
    juego = TaTeTi(root)
    root.mainloop()



