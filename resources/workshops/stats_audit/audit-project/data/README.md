# Palmer Penguins data

`penguins.csv` is the `penguins` table from the palmerpenguins package, distributed as a plain CSV. It has 344 rows, one per penguin, and eight columns.

| Column | Meaning |
|---|---|
| `species` | Adelie, Chinstrap, or Gentoo |
| `island` | Biscoe, Dream, or Torgersen |
| `bill_length_mm`, `bill_depth_mm` | Bill measurements in millimeters |
| `flipper_length_mm` | Flipper length in millimeters |
| `body_mass_g` | Body mass in grams |
| `sex` | female or male |
| `year` | Sampling year, 2007 to 2009 |

Missing values are written as the literal `NA` (pandas reads them as missing). The file is unchanged from the source.

## Source and license

- Data collected and made available by Dr. Kristen Gorman and the Palmer Station Long Term Ecological Research (LTER) program. Original study: Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus *Pygoscelis*). *PLoS ONE* 9(3): e90081.
- Packaged for R by Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version 0.1.0. The [package site](https://allisonhorst.github.io/palmerpenguins/) states the data are available under a CC0 license.
- File retrieved from the [package repository](https://github.com/allisonhorst/palmerpenguins/blob/main/inst/extdata/penguins.csv) on September 28, 2026.
