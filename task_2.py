import turtle


def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.right(45)
    draw_pifagor_tree(0.6 * branch_len, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.6 * branch_len, level - 1)
    turtle.right(45)
    turtle.backward(branch_len)


def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    level = int(input("Введіть рівень рекурсії: "))  # Користувач вводить рівень рекурсії
    draw_pifagor_tree(150, level)  # Початкова довжина гілки та вказаний користувачем рівень рекурсії

    turtle.done()


main()