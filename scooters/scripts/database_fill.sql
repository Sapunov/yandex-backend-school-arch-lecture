-- 10 random records
-- INSERT INTO scooters
-- SELECT
--        uuid_generate_v4() AS id,
--        POINT(37+random(), 55+random()) AS location,
--        (CASE WHEN random() > 0.5 THEN uuid_generate_v4() ELSE NULL END) AS "user"
-- FROM generate_series(1, 10)

-- or via insert statements
INSERT INTO scooters (id, location, "user") VALUES ('58c5080f-6726-42f3-a997-f143ad984201', '(37.46829361638372,55.05982583193995)', null);
INSERT INTO scooters (id, location, "user") VALUES ('8f484690-f92b-417e-9b68-2bd58f1ed700', '(37.05780740487775,55.683570543711426)', null);
INSERT INTO scooters (id, location, "user") VALUES ('becd1d25-1ab8-4f89-a310-e8177a94093f', '(37.94867354172965,55.313234742670744)', 'df65a1d8-e3c5-452d-a5b0-4e8b8abd55d3');
INSERT INTO scooters (id, location, "user") VALUES ('917e9894-0822-4a33-9bfc-5121b937b637', '(37.14825826460845,55.00325180712231)', null);
INSERT INTO scooters (id, location, "user") VALUES ('5f32966e-87c9-4725-bf18-3d8439044c11', '(37.14117043538411,55.131343164062876)', null);
INSERT INTO scooters (id, location, "user") VALUES ('45bec7d8-b60e-4fc0-9752-c0b3f6d204ee', '(37.70299881637874,55.75460344872543)', null);
INSERT INTO scooters (id, location, "user") VALUES ('5898c44f-bfb8-4b6f-a14a-36e5797828b1', '(37.0970577108166,55.644623924666305)', null);
INSERT INTO scooters (id, location, "user") VALUES ('abfbb1f6-c9b5-47a5-9f4f-0da16763310b', '(37.238075893682485,55.157759477336185)', null);
INSERT INTO scooters (id, location, "user") VALUES ('0533e457-40f9-468a-ba70-4f1903b55d6b', '(37.26313503696669,55.3111815759084)', null);
INSERT INTO scooters (id, location, "user") VALUES ('aff866f5-6877-4eea-9c19-b90980dd0d65', '(37.446735940409766,55.702897019510004)', null);
