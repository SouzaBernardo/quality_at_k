class Interpolation: 
    def __init__(self):
        pass



    def interpolate_1d(self, x, y, x_interp):
        from scipy.interpolate import interp1d
        f = interp1d(x, y)
        y_interp = f(x_interp)
        return y_interp.tolist()
    @staticmethod
    def interpolate_2d(x, y, z, x_interp, y_interp):
        points = np.array([x, y]).T
        values = np.array(z)
        grid_x, grid_y = np.meshgrid(x_interp, y_interp)
        z_interp = griddata(points, values, (grid_x, grid_y), method='linear')
        return z_interp.tolist()