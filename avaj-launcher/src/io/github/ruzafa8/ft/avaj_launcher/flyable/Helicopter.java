package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.Coordinates;
import io.github.ruzafa8.ft.avaj_launcher.OutputFileWriter;

public class Helicopter extends Aircraft {
    public Helicopter(long id, String name, Coordinates coordinates) {
        super(id, name, coordinates);
    }

    @Override
    public void updateConditions() {
        String weather = this.weatherTower.getWeather(this.coordinates);
        switch (weather) {
            case "SUN":
                this.coordinates.offsetCoordinates(10, 0, 2);
                OutputFileWriter.write(getCode() + ": Helicopter, helicopter...");
                break;
            case "RAIN":
                this.coordinates.offsetCoordinates(5, 0, 0);
                OutputFileWriter.write(getCode() + ": What a storm!!");
                break;
            case "FOG":
                this.coordinates.offsetCoordinates(1, 0, 0);
                OutputFileWriter.write(getCode() + ": Mayday, mayday, mayday! A dense fog is surrounding us!");
                break;
            case "SNOW":
                this.coordinates.offsetCoordinates(0, 0, -12);
                OutputFileWriter.write(getCode() + ": My rotor is going to freeze.");
                break;
        }
        super.updateConditions();
    }
}
