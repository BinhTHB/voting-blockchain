# Graph Report - .  (2026-04-09)

## Corpus Check
- Corpus is ~41,138 words - fits in a single context window. You may not need a graph.

## Summary
- 135 nodes · 154 edges · 26 communities detected
- Extraction: 82% EXTRACTED · 17% INFERRED · 1% AMBIGUOUS · INFERRED: 26 edges (avg confidence: 0.66)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Block` - 13 edges
2. `Blockchain` - 12 edges
3. `VOSY Web Interface (vosy_app/vosy.py)` - 5 edges
4. `Peer2 instance (127.0.0.1:4000)` - 5 edges
5. `Peer3 instance (127.0.0.1:4001)` - 5 edges
6. `Orderer (bottom_left)` - 5 edges
7. `Survey post card: "127.0.0.1:5000 made a post with id 1."` - 5 edges
8. `compute_open_surveys()` - 4 edges
9. `Peer (bcb_server/peer.py)` - 4 edges
10. `Peer1 instance (127.0.0.1:5000)` - 4 edges

## Surprising Connections (you probably didn't know these)
- `VOSY Web Interface (vosy_app/vosy.py)` --references--> `Flask`  [INFERRED]
  vosy_app/vosy.py → requirements.txt
- `Peer (bcb_server/peer.py)` --references--> `Requests`  [INFERRED]
  bcb_server/peer.py → requirements.txt
- `VOSY Interface 1 (127.0.0.1:8080 -> Peer 5000)` --implements--> `VOSY Web Interface (vosy_app/vosy.py)`  [EXTRACTED]
  README.md → vosy_app/vosy.py
- `Peer1 instance (127.0.0.1:5000)` --shares_data_with--> `Orderer (bcb_server/orderer.py)`  [EXTRACTED]
  README.md → bcb_server/orderer.py
- `Peer2 instance (127.0.0.1:4000)` --shares_data_with--> `Orderer (bcb_server/orderer.py)`  [EXTRACTED]
  README.md → bcb_server/orderer.py

## Hyperedges (group relationships)
- **Cluster 1 (main node & infrastructure)** — bcb_server_orderer_py, bcb_server_certificate_authority_py, peer_instance_5000, vosy_instance_8080 [EXTRACTED 1.00]
- **Cluster 2 (peer 2 & interface 2)** — peer_instance_4000, vosy_instance_8081 [EXTRACTED 1.00]
- **Cluster 3 (peer 3 & interface 3)** — peer_instance_4001, vosy_instance_8082 [EXTRACTED 1.00]
- **Orderer cluster** — network_sample_orderer_top, network_sample_orderer_bottom_left, network_sample_orderer_bottom_right [INFERRED 0.85]
- **Top orderer and peers** — network_sample_orderer_top, network_sample_peer_top_above, network_sample_peer_top_left, network_sample_peer_top_right [EXTRACTED 1.00]
- **Bottom-left orderer and peers** — network_sample_orderer_bottom_left, network_sample_peer_bl_left, network_sample_peer_bl_bottom, network_sample_peer_bl_center [EXTRACTED 1.00]
- **Bottom-right orderer and peers** — network_sample_orderer_bottom_right, network_sample_peer_br_left, network_sample_peer_br_right [EXTRACTED 1.00]
- **Post New Survey form fields** — sample_post_new_survey_form, sample_field_question_id, sample_field_survey, sample_field_answer, sample_field_opening_time, sample_submit_button [EXTRACTED 1.00]
- **Open Surveys contains survey cards** — sample_open_surveys_section, sample_survey_card_1 [EXTRACTED 1.00]
- **Machine (left) composition** — architecture_vosy_left, architecture_peer_left [EXTRACTED 1.00]
- **Machine (center) composition** — architecture_vosy_center, architecture_peer_center, architecture_ca_center, architecture_orderer_center [EXTRACTED 1.00]
- **Machine (right) composition** — architecture_vosy_right [EXTRACTED 1.00]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.11
Nodes (17): Block, fromDict(), A function that return the hash of the block contents., Blockchain, check_chain_validity(), fromList(), is_valid_proof(), A function to generate genesis block and appends it to         the chain. The bl (+9 more)

### Community 1 - "Community 1"
Cohesion: 0.2
Nodes (15): Certificate Authority (bcb_server/certificate_authority.py), Orderer (bcb_server/orderer.py), Peer (bcb_server/peer.py), Document language: vi-VN (Vietnamese), Peer2 instance (127.0.0.1:4000), Peer3 instance (127.0.0.1:4001), Peer1 instance (127.0.0.1:5000), Avoid port collisions (use distinct ports) (+7 more)

### Community 2 - "Community 2"
Cohesion: 0.13
Nodes (9): close_survey(), fetch_posts(), index(), Endpoint to create a new transaction via our application., Endpoint to create a new transaction via our application., Endpoint to create a new transaction via our application., Function to fetch the chain from a blockchain node, parse the     data and store, submit_textarea() (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.19
Nodes (7): compute_open_surveys(), get_chain(), get_open_surveys(), mine_unconfirmed_transactions(), This function serves as an interface to add the pending     transactions to the, validate_and_add_block(), validate_transaction()

### Community 4 - "Community 4"
Cohesion: 0.18
Nodes (11): Orderer (bottom_left), Orderer (bottom_right), Orderer (top), Peer (bottom of bottom-left orderer), Peer (bottom-center near bottom-left orderer), Peer (left of bottom-left orderer), Peer (left of bottom-right orderer), Peer (right of bottom-right orderer) (+3 more)

### Community 5 - "Community 5"
Cohesion: 0.25
Nodes (8): User avatar (illustration) on card, Red circular X (delete/close icon) on card, Blockchain (system concept), 127.0.0.1:5000 (post author/source), Post New Survey (form), Submit (form button), Survey post card: "127.0.0.1:5000 made a post with id 1.", Survey id 1

### Community 6 - "Community 6"
Cohesion: 0.4
Nodes (0): 

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (5): Orderer (center) Port: 5002, Peer (center) Port: 5000, Peer (left) Port: 5000, Port 5000, Port 5002

### Community 8 - "Community 8"
Cohesion: 0.83
Nodes (4): Port 8080, Vosy (center) Port: 8080, Vosy (left) Port: 8080, Vosy (right) Port: 8080

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (0): 

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (2): 0.0.0.0:8080 (address bar), A Simple Blockchain based Voting System

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (2): Mine (action: block creation/mining), Mine (button)

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (2): Update Chaincode (action), Update Chaincode (button)

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (2): Resync (action: network/state resync), Resync (button)

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (2): View Pending Transactions (action), Pending Transaction (button)

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (2): List Nodes (action), List Node (button)

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (2): Certificate Authority (CA) (center) Port: 5001, Port 5001

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (1): BCB_VOSY (brand/home link)

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (1): Question ID field

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (1): Survey textarea field

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (1): Answer field

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (1): Opening Time (minute) field

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (1): Open Surveys (section)

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (1): Machine (left)

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (1): Machine (center)

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (1): Machine (right)

## Ambiguous Edges - Review These
- `VOSY Web Interface (vosy_app/vosy.py)` → `bcb_vosy.pdf`  [AMBIGUOUS]
  docs/bcb_vosy.pdf · relation: conceptually_related_to
- `Survey post card: "127.0.0.1:5000 made a post with id 1."` → `Red circular X (delete/close icon) on card`  [AMBIGUOUS]
  docs/sample.png · relation: conceptually_related_to

## Knowledge Gaps
- **45 isolated node(s):** `Function to fetch the chain from a blockchain node, parse the     data and store`, `Endpoint to create a new transaction via our application.`, `Endpoint to create a new transaction via our application.`, `Endpoint to create a new transaction via our application.`, `Check if block_hash is valid hash of block and satisfies         the difficulty` (+40 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 9`** (2 nodes): `chaincode.py`, `count_down_opening_time()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `0.0.0.0:8080 (address bar)`, `A Simple Blockchain based Voting System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (2 nodes): `Mine (action: block creation/mining)`, `Mine (button)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (2 nodes): `Update Chaincode (action)`, `Update Chaincode (button)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `Resync (action: network/state resync)`, `Resync (button)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `View Pending Transactions (action)`, `Pending Transaction (button)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (2 nodes): `List Nodes (action)`, `List Node (button)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `Certificate Authority (CA) (center) Port: 5001`, `Port 5001`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (1 nodes): `BCB_VOSY (brand/home link)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `Question ID field`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (1 nodes): `Survey textarea field`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `Answer field`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `Opening Time (minute) field`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `Open Surveys (section)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `Machine (left)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `Machine (center)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `Machine (right)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.