import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FS = 14
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
fig.patch.set_facecolor('white')

def caixa(ax, x, y, w, h, texto, cor_fundo, cor_borda, bold=False, fs=FS):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.1",
                         facecolor=cor_fundo, edgecolor=cor_borda,
                         linewidth=2.0, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, texto, ha='center', va='center',
            fontsize=fs, fontweight='bold' if bold else 'normal',
            color='#1a1a1a', multialignment='center',
            zorder=4, linespacing=1.5)

def seta(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#555555',
                                lw=1.8, connectionstyle='arc3,rad=0.0'),
                zorder=2)

ax.text(7.0, 9.7, 'Organização e Balanceamento dos Dados',
        ha='center', va='center', fontsize=16,
        fontweight='bold', color='#1a1a1a')

caixa(ax, 3.2, 8.9, 5.5, 0.9, 'UA-Speech  |  fala disártrica\n41.260 áudios (.wav)', '#D6E4F0', '#2980B9')
caixa(ax, 10.2, 8.9, 5.5, 0.9, 'Free Spoken Digit Dataset  |  fala típica\n30.000 áudios (.wav)', '#D5F5E3', '#27AE60')

caixa(ax, 3.2, 7.6, 5.5, 0.9, 'Rotulação: padrão _D0_ ... _D9_\nno nome do arquivo', '#EBF5FB', '#2980B9')
caixa(ax, 10.2, 7.6, 5.5, 0.9, 'Rotulação: primeiro\ncaractere do nome do arquivo', '#EAFAF1', '#27AE60')
seta(ax, 3.2, 8.45, 3.2, 8.05)
seta(ax, 10.2, 8.45, 10.2, 8.05)

caixa(ax, 1.5, 6.3, 2.5, 0.9, 'Dígitos (0–9)\n5.630 amostras', '#FDFEFE', '#2980B9')
caixa(ax, 4.8, 6.3, 2.5, 0.9, 'nao_numero\n35.630 amostras', '#FDEDEC', '#E74C3C')
caixa(ax, 10.2, 6.3, 5.5, 0.9, 'Dígitos (0–9)\n30.000 amostras', '#FDFEFE', '#27AE60')
seta(ax, 3.2, 7.15, 1.5, 6.75)
seta(ax, 3.2, 7.15, 4.8, 6.75)
seta(ax, 10.2, 7.15, 10.2, 6.75)

caixa(ax, 7.0, 5.1, 10.5, 0.9,
      'Dígitos combinados (0–9)  —  5.630 (disartria) + 30.000 (normal) = 35.630 amostras',
      '#EAF2F8', '#2471A3')
seta(ax, 1.5, 5.85, 4.0, 5.55)
seta(ax, 10.2, 5.85, 10.0, 5.55)

caixa(ax, 4.8, 3.95, 3.8, 0.9, 'Subamostragem aleatória\nnao_numero → 35.630', '#FDEDEC', '#E74C3C')
seta(ax, 4.8, 5.85, 4.8, 4.40)

caixa(ax, 7.0, 2.8, 12.5, 1.0,
      'Conjunto unificado e embaralhado  |  71.260 amostras  |  11 classes\n35.630 dígitos (5.630 disartria + 30.000 normal)  |  35.630 nao_numero',
      '#F4ECF7', '#8E44AD', bold=True)
seta(ax, 7.0, 4.50, 7.0, 3.30)
seta(ax, 4.8, 3.50, 5.8, 3.30)

caixa(ax, 3.5, 1.5, 5.5, 0.9, 'Treinamento\n49.881 amostras  (70%)', '#FEF9E7', '#D4AC0D')
caixa(ax, 10.5, 1.5, 5.5, 0.9, 'Teste\n21.379 amostras  (30%)', '#FEF9E7', '#D4AC0D')
seta(ax, 5.5, 2.30, 4.5, 1.95)
seta(ax, 8.5, 2.30, 9.5, 1.95)
ax.text(7.0, 1.5, 'Estratificada por origem e rótulo',
        ha='center', va='center', fontsize=12,
        color='#7D6608', style='italic')

plt.tight_layout(pad=0.3)
plt.savefig('fluxo_dados.jpg', dpi=180, bbox_inches='tight',
            facecolor='white', format='jpg', pil_kwargs={'quality': 90})
plt.show()
print("Salvo: fluxo_dados.jpg")
