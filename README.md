# Valnatt
This is a tool to monitor the Swedish election on the election night.

Valnatt (_Swedish for election night_) pulls data from the Swedish Election Authority and dispalys it in a graph. You can view the preliminary results per region and election (parlament, county, and municipality).

## Election types
- *R*: Riksdag (Parlament)
- *L*: Länsting (County)
- *K*: Kommun (municipality)

## Examples
### How **Sweden** votes for the **parlament**
http://127.0.0.1:5000/valnatt/?region=0&election=R

### How **Österåker** (municipality) votes for the **parlament**
http://127.0.0.1:5000/valnatt/?region=0117&election=R

### How **Österåker** (municipality) votes for the **town council**
http://127.0.0.1:5000/valnatt/?region=0117&election=K