
# Gazetteer Service

## Overview

The gazetteer service provides a local, authoritative source for place name and geographic information.
It implements the following services:

  1. Given a place name, provide a list of possible matching identifiers. This resolution
will handle synonyms.
  2. Given a place identifier, provide information about the place  such
as coordinates, and the canonical version of the name. A listing of the data fields
is given below.
  3. Given a coordinate, try to provide a place identifier and name.
  4. Given an initial segment of a place name, provide a list of possible completions.

The information provided for each place name includes the following.
More information may be provided.

  1. Canonical name(s)
  2. List of (non-canonical) alternate names. Possibly empty.
  3. Our local identifier (LID) for the place
  4. Other identifiers, if available. Possible sources: NGA Geonames, Geonames.org, Yahoo Geo., Getty
  5. Date modified (for our record)
  6. Containing continent (see list below for valid values)
  7. Containing country, both country code and the LID
  8. Containing adm1 unit, as text and as LID, if available
  9. Optional containing admin2 unit, as text and LID, if available
  10. Coordinate (lat long) in decimal degress north and east. Coordinate refers to the centroid of the place.
  11. Optional bounding box (north-west and south-east corners, in decimal degrees)
  12. Feature type code (see list below for valid values)
  13. The source of the record (local, NGA, geonames.org, other)
  14. Parent record(s). May be one or more for both physical parent and political parent.
  15. Children records(s).

List of continent names:

    1. TBD

List of place categories:

    1. TBD

Each place record is the composite of 1 or more source records.
Source records may be either locally generated, or come from an external authority.
The gazetteer allows place names to be "labeled", and queries can be restricted by label.



# API

This service is a data API.
The requests are made using HTTP requests, and the responses are JSON documents.
The API is broken into those commands which _query_ the service, and those which _manage_ it.

## Query API



## Management API

The management API requires an understanding of the internal storage of the place records.
See below.

# Internal Record Structure

There are two kinds of records: place records and source records.
A source record consists of

    1. A local identifier
    2. A source authority (format TBD)
    3. A remote record id
    4. A modification date (for when this source record was changed...not for when the remote data was updated)
    5. An arbitrary number of fields + data. Format TBD (perhaps RDF?)

A place record consists of

    1. A local identifier
    2. An ordered list of pairs of source record local identifiers and either a '+' or 's'
    3. An optional data cache

The optional data cache is the composite of all the source records.
The order source records are listed is important.
The algorithm to composite the records is as follows:

    * Let L = (s_0, m_0), (s_1, m_1), (s_2, m_2) ... be a list of source record ids and modifiers.
    * We start with an empty set of properties P.
    * We iterate through the list in order:
        * given (s_i, m_i) the field data in the source record s_i either replaces the corresponding fields in P, if
        m_i is 's' (for _supersedes_), or is appended to the corresponding fields of P, if m_i is '+'


