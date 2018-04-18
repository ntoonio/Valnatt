# Valnatt

## "Kombinationer"
Den här delen visar vilka olika kombinationer av data som ska visas.

### Kommun krets
#### Hur *kommunkrets* i kommunvalet
	<LÄNSKOD><KOMMUNKOD>K / KOMMUN / KRETS_KOMMUN / KOD == <LÄNSKOD><KOMMUNKOD><KRETS_KOD> / GILTIGA
	0117K / kommun / krets_kommun / kod == 011701 / giltiga

#### Hur *kommunkrets* i landstingsvalet
	<LÄNSKOD><KOMMUNKOD>L / KOMMUN / KRETS_KOMMUN / KOD == <LÄNSKOD><KOMMUNKOD><KRETS_KOD> / GILTIGA
	0117L / kommun / krets_kommun / kod == 011701 / giltiga

#### Hur *kommunkrets* röstade i riksdagsvalet
	<LÄNSKOD><KOMMUNKOD>R / KOMMUN / KRETS_KOMMUN / KOD == <LÄNSKOD><KOMMUNKOD><KRETS_KOD> / GILTIGA
	0117R / kommun / krets_kommun / kod == 011701 / giltiga

### Kommun
#### Hur *kommun* röstade i kommun-valet
	<LÄNSKOD><KOMMUNKOD>K / KOMMUN / GILTIGA
	0117K / kommun / giltiga

#### Hur *kommun* röstade i landstings-valet
	<LÄNSKOD><KOMMUNKOD>L / KOMMUN / GILTIGA
	0117L / kommun / giltiga

#### Hur *kommun* röstade i riksdags-valet
	<LÄNSKOD><KOMMUNKOD>R / KOMMUN / GILTIGA
	0117R / kommun / giltiga

### Län
#### Hur *län* röstade i landstings-valet
	00L / NATION / LÄN / KOD == <LÄNSKOD> / GILTIGA
	00L / nation / län / kod == 01 / giltiga

#### Hur *län* röstade i riksdags-valet
	00R / NATION / LÄN / KOD == <LÄNSKOD> / GILTIGA
	00R / nation / län / kod == 01 / giltiga

### Nation
#### Hur *nationen* röstade i riksdags-valet
	00R / NATION / GILTIGA
	00R / nation / giltiga