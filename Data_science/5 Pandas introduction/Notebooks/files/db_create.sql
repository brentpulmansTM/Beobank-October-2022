CREATE TABLE "customers" (
	"customerID"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("customerID")
);

CREATE TABLE "purchases" (
	"purchasesID"	INTEGER NOT NULL,
	"customerID"	INTEGER,
	"quantity"		INTEGER,
	"fruit"			TEXT,
	FOREIGN KEY("customerID") REFERENCES "customers"("customerID"),
	PRIMARY KEY("purchasesID")
);

INSERT INTO "customers" VALUES ( 1, "June");
INSERT INTO "customers" VALUES ( 2, "Robert");
INSERT INTO "customers" VALUES ( 3, "Lily");
INSERT INTO "customers" VALUES ( 4, "David");

INSERT INTO "purchases" VALUES ( 1, 1, 3, "apples");
INSERT INTO "purchases" VALUES ( 2, 2, 2, "apples");
INSERT INTO "purchases" VALUES ( 3, 3, 0, "apples");
INSERT INTO "purchases" VALUES ( 4, 4, 1, "apples");
INSERT INTO "purchases" VALUES ( 5, 1, 0, "oranges");
INSERT INTO "purchases" VALUES ( 6, 2, 3, "oranges");
INSERT INTO "purchases" VALUES ( 7, 3, 7, "oranges");
INSERT INTO "purchases" VALUES ( 8, 4, 2, "oranges");