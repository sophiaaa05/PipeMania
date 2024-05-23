PY=python3.8
SRC=codigo_base/pipe.py
TEST_DIR=tests

TESTS=$(wildcard $(TEST_DIR)/*.txt)
DIFFS=$(patsubst $(TEST_DIR)/%.txt, $(TEST_DIR)/%.diff, $(TESTS))

run: $(SRC)
	@ $(PY) $(SRC)

test: clean $(DIFFS)

.PRECIOUS: $(TEST_DIR)/%.myout
$(TEST_DIR)/%.diff: $(TEST_DIR)/%.out $(TEST_DIR)/%.myout
	-@diff $^ > $@

$(TEST_DIR)/%.myout: $(TEST_DIR)/%.txt $(SRC)
	@echo $@ >> $(TEST_DIR)/err.myout
	-@$(PY) $(SRC) < $< > $@ 2>> $(TEST_DIR)/err.myout

clean:
	-$(RM) $(TEST_DIR)/*.myout
	-$(RM) $(TEST_DIR)/*.diff

view:
	@cd Visualizador && $(PY) visualizer.py
