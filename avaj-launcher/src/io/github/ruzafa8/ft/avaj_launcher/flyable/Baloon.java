package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.Coordinates;
import io.github.ruzafa8.ft.avaj_launcher.OutputFileWriter;

public class Baloon extends Aircraft {
    public Baloon(long id, String name, Coordinates coordinates) {
        super(id, name, coordinates);
    }

    @Override
    public void updateConditions() {
        String weather = this.weatherTower.getWeather(this.coordinates);
        switch (weather) {
            case "SUN":
                this.coordinates.offsetCoordinates(2, 0, 4);
                OutputFileWriter.write(getCode() + ": let's enjoy the good weather.");
                break;
            case "RAIN":
                this.coordinates.offsetCoordinates(0, 0, -5);
                OutputFileWriter.write(getCode() + ": Damn you rain! You messed up my baloon.");
                break;
            case "FOG":
                this.coordinates.offsetCoordinates(0, 0, -3);
                OutputFileWriter.write(getCode() + ": Cannot see anything with this fog.");
                break;
            case "SNOW":
                this.coordinates.offsetCoordinates(0, 0, -15);
                OutputFileWriter.write(getCode() + ": It's snowing. We're gonna crash.");
        }
        super.updateConditions();
    }
}
