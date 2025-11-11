import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 10, value=5, label="周波数")
    slider
    return (slider,)


@app.cell
def _(slider):
    # cell: スライダーの値に応じて描画
    import numpy as np
    import matplotlib.pyplot as plt

    # スライダーの値を取得
    freq = slider.value

    # データ生成
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.sin(freq * x)

    # 描画
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"sin({freq}x)")
    ax.grid(True)
    fig
    return


if __name__ == "__main__":
    app.run()
