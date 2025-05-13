import math

# Вхідні дані
azimuth_deg = 335  # азимут "вгору"
scale = 0.38  # м на піксель

# Роздільна здатність зображення
img_width = 640
img_height = 512

# Центр зображення
center_x = 320
center_y = 256

# Піксельні координати контрольної точки
point_x_center = 558
point_y_center = 328

# Географічні координати контрольної точки
lat_ref = 50.603694
lon_ref = 30.650625

# Обчислюємо відстань у пікселях по X та Y
dx_pixels = center_x - point_x_center
dy_pixels = center_y - point_y_center

# Повертаємо систему координат з урахуванням азимута
azimuth_rad = math.radians(azimuth_deg)
dx_m = (math.cos(azimuth_rad) * dx_pixels + math.sin(azimuth_rad) * dy_pixels) * scale
dy_m = (-math.sin(azimuth_rad) * dx_pixels + math.cos(azimuth_rad) * dy_pixels) * scale

# Перетворення зсуву у географічні координати
lat_center = lat_ref + dy_m / 111320
lon_center = lon_ref + dx_m / (111320 * math.cos(math.radians(lat_ref)))

print(f"Центр зображення: широта = {lat_center:.6f}, довгота = {lon_center:.6f}")
