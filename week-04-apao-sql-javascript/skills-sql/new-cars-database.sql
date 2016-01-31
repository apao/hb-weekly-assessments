--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: awards; Type: TABLE; Schema: public; Owner: apao; Tablespace: 
--

CREATE TABLE awards (
    id integer NOT NULL,
    award_name character varying(50) NOT NULL,
    year integer NOT NULL,
    winner_model_id integer
);


ALTER TABLE awards OWNER TO apao;

--
-- Name: awards_id_seq; Type: SEQUENCE; Schema: public; Owner: apao
--

CREATE SEQUENCE awards_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE awards_id_seq OWNER TO apao;

--
-- Name: awards_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: apao
--

ALTER SEQUENCE awards_id_seq OWNED BY awards.id;


--
-- Name: brands; Type: TABLE; Schema: public; Owner: apao; Tablespace: 
--

CREATE TABLE brands (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    founded integer,
    headquarters character varying(50),
    discontinued integer
);


ALTER TABLE brands OWNER TO apao;

--
-- Name: brands_id_seq; Type: SEQUENCE; Schema: public; Owner: apao
--

CREATE SEQUENCE brands_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE brands_id_seq OWNER TO apao;

--
-- Name: brands_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: apao
--

ALTER SEQUENCE brands_id_seq OWNED BY brands.id;


--
-- Name: models; Type: TABLE; Schema: public; Owner: apao; Tablespace: 
--

CREATE TABLE models (
    id integer NOT NULL,
    year integer NOT NULL,
    brand_name character varying(50),
    name character varying(50) NOT NULL
);


ALTER TABLE models OWNER TO apao;

--
-- Name: models_id_seq; Type: SEQUENCE; Schema: public; Owner: apao
--

CREATE SEQUENCE models_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE models_id_seq OWNER TO apao;

--
-- Name: models_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: apao
--

ALTER SEQUENCE models_id_seq OWNED BY models.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: apao
--

ALTER TABLE ONLY awards ALTER COLUMN id SET DEFAULT nextval('awards_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: apao
--

ALTER TABLE ONLY brands ALTER COLUMN id SET DEFAULT nextval('brands_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: apao
--

ALTER TABLE ONLY models ALTER COLUMN id SET DEFAULT nextval('models_id_seq'::regclass);


--
-- Data for Name: awards; Type: TABLE DATA; Schema: public; Owner: apao
--

COPY awards (id, award_name, year, winner_model_id) FROM stdin;
1	IIHS Safety Award	2015	50
2	IIHS Safety Award	2015	51
\.


--
-- Name: awards_id_seq; Type: SEQUENCE SET; Schema: public; Owner: apao
--

SELECT pg_catalog.setval('awards_id_seq', 2, true);


--
-- Data for Name: brands; Type: TABLE DATA; Schema: public; Owner: apao
--

COPY brands (id, name, founded, headquarters, discontinued) FROM stdin;
1	Ford	1903	Dearborn, MI	\N
2	Chrysler	1925	Auburn Hills, Michigan	\N
3	Citroën	1919	Saint-Ouen, France	\N
4	Hillman	1907	Ryton-on-Dunsmore, England	1981
5	Chevrolet	1911	Detroit, Michigan	\N
6	Cadillac	1902	New York City, NY	\N
7	BMW	1916	Munich, Bavaria, Germany	\N
8	Austin	1905	Longbridge, England	1987
9	Fairthorpe	1954	Chalfont St Peter, Buckinghamshire	1976
10	Studebaker	1852	South Bend, Indiana	1967
11	Pontiac	1926	Detroit, MI	2010
12	Buick	1903	Detroit, MI	\N
13	Rambler	1901	Kenosha, Washington	1969
14	Plymouth	1928	Auburn Hills, Michigan	2001
15	Tesla	2003	Palo Alto, CA	\N
\.


--
-- Name: brands_id_seq; Type: SEQUENCE SET; Schema: public; Owner: apao
--

SELECT pg_catalog.setval('brands_id_seq', 15, true);


--
-- Data for Name: models; Type: TABLE DATA; Schema: public; Owner: apao
--

COPY models (id, year, brand_name, name) FROM stdin;
1	1909	Ford	Model T
2	1926	Chrysler	Imperial
3	1948	Citroën	2CV
4	1950	Hillman	Minx Magnificent
5	1953	Chevrolet	Corvette
6	1954	Chevrolet	Corvette
7	1954	Cadillac	Fleetwood
8	1955	Chevrolet	Corvette
9	1955	Ford	Thunderbird
10	1956	Chevrolet	Corvette
11	1957	Chevrolet	Corvette
12	1957	BMW	600
13	1958	Chevrolet	Corvette
14	1958	BMW	600
15	1958	Ford	Thunderbird
16	1959	Austin	Mini
17	1959	Chevrolet	Corvette
18	1959	BMW	600
19	1960	Chevrolet	Corvair
20	1960	Chevrolet	Corvette
21	1960	Fillmore	Fillmore
22	1960	Fairthorpe	Rockette
23	1961	Austin	Mini Cooper
24	1961	Studebaker	Avanti
25	1961	Pontiac	Tempest
26	1961	Chevrolet	Corvette
27	1962	Pontiac	Grand Prix
28	1962	Chevrolet	Corvette
29	1962	Studebaker	Avanti
30	1962	Buick	Special
31	1963	Austin	Mini
32	1963	Austin	Mini Cooper S
33	1963	Rambler	Classic
34	1963	Ford	E-Series
35	1963	Studebaker	Avanti
36	1963	Pontiac	Grand Prix
37	1963	Chevrolet	Corvair 500
38	1963	Chevrolet	Corvette
39	1964	Chevrolet	Corvette
40	1964	Ford	Mustang
41	1964	Ford	Galaxie
42	1964	Pontiac	GTO
43	1964	Pontiac	LeMans
44	1964	Pontiac	Bonneville
45	1964	Pontiac	Grand Prix
46	1964	Plymouth	Fury
47	1964	Studebaker	Avanti
48	1964	Austin	Mini Cooper
50	2015	Chevrolet	Malibu
51	2015	Subaru	Outback
\.


--
-- Name: models_id_seq; Type: SEQUENCE SET; Schema: public; Owner: apao
--

SELECT pg_catalog.setval('models_id_seq', 51, true);


--
-- Name: awards_pkey; Type: CONSTRAINT; Schema: public; Owner: apao; Tablespace: 
--

ALTER TABLE ONLY awards
    ADD CONSTRAINT awards_pkey PRIMARY KEY (id);


--
-- Name: brands_pkey; Type: CONSTRAINT; Schema: public; Owner: apao; Tablespace: 
--

ALTER TABLE ONLY brands
    ADD CONSTRAINT brands_pkey PRIMARY KEY (id);


--
-- Name: models_pkey; Type: CONSTRAINT; Schema: public; Owner: apao; Tablespace: 
--

ALTER TABLE ONLY models
    ADD CONSTRAINT models_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: apao
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM apao;
GRANT ALL ON SCHEMA public TO apao;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

