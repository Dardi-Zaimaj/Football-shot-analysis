from statsbombpy import sb
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import pandas as pd

# Load events and filter shots
events = sb.events(match_id=3895232)
shots = events[events['type'] == 'Shot'].copy()

# Split into two teams
leverkusen = shots[shots['team'] == 'Bayer Leverkusen']
bayern = shots[shots['team'] == 'Bayern Munich']

# Set up the pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='#1a1a2e', line_color='white')
fig, ax = pitch.draw(figsize=(12, 8))
fig.patch.set_facecolor('#1a1a2e')

# Plot Leverkusen shots
for _, shot in leverkusen.iterrows():
    x, y = shot['location'][0], shot['location'][1]
    xg = shot['shot_statsbomb_xg']
    outcome = shot['shot_outcome']
    color = '#e63946' if outcome == 'Goal' else '#a8dadc'
    pitch.scatter(x, y, ax=ax, s=xg*1500, color=color,
                  edgecolors='white', linewidth=0.8, alpha=0.85, zorder=3)

# Plot Bayern shots
for _, shot in bayern.iterrows():
    x, y = shot['location'][0], shot['location'][1]
    xg = shot['shot_statsbomb_xg']
    outcome = shot['shot_outcome']
    color = '#e63946' if outcome == 'Goal' else '#f4a261'
    pitch.scatter(120 - x, 80 - y, ax=ax, s=xg*1500, color=color,
                  edgecolors='white', linewidth=0.8, alpha=0.85, zorder=3)

# Title and legend
ax.set_title('Bayer Leverkusen vs Bayern Munich\nBundesliga 2023/24 — Shot Map',
             color='white', fontsize=14, fontweight='bold', pad=15)

# Legend
ax.scatter([], [], color='#a8dadc', s=150, edgecolors='white', label='Leverkusen shot')
ax.scatter([], [], color='#f4a261', s=150, edgecolors='white', label='Bayern shot')
ax.scatter([], [], color='#e63946', s=150, edgecolors='white', label='Goal')
ax.text(0.01, 0.02, 'Bubble size = xG value', transform=ax.transAxes,
        color='white', fontsize=9, alpha=0.7)
ax.legend(loc='upper left', facecolor='#1a1a2e', labelcolor='white',
          framealpha=0.5, fontsize=9)

plt.tight_layout()
plt.savefig('/Users/chriszaimi/Desktop/shot_map_leverkusen_bayern.png', dpi=150, bbox_inches='tight')
plt.show()
print("Shot map saved!")