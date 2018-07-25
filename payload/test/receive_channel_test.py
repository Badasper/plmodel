from model.receive_channel import ReceiveRFChannel


class TestCaseReceiveChannel:

    def test_down_convert_channel(self):
        ch_lo_bigger = ReceiveRFChannel(intermediate_frequency=5,
                                        local_oscillator_frequency=8,
                                        bandwidth_channel=1)
        assert ch_lo_bigger.main_receive(convert='down')['center'] == 13
        assert ch_lo_bigger.image_receive(convert='down')['center'] == 3
        assert ch_lo_bigger.intermediate_receive()['center'] == 5
        assert len(ch_lo_bigger.combinations_receive()) == 207
        for item in ch_lo_bigger.combinations_receive():
            print(item)
        assert len(ch_lo_bigger.equal_nm_receive()) == 20
        assert len(ch_lo_bigger.get_all_combinations()) == 210

        ch_lo_less = ReceiveRFChannel(intermediate_frequency=5,
                                      local_oscillator_frequency=3,
                                      bandwidth_channel=2)
        assert ch_lo_less.main_receive(convert='down')['center'] == 8
        assert ch_lo_less.image_receive(convert='down')['center'] == 2

    def test_error_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=5,
                              local_oscillator_frequency=3,
                              bandwidth_channel=1)
        try:
            ch.main_receive(convert='next')
        except ValueError:
            pass
        try:
            ch.image_receive(convert='next')
        except ValueError:
            pass

    def test_up_convert_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=10,
                              local_oscillator_frequency=3,
                              bandwidth_channel=1)

        assert ch.image_receive(convert='up')['center'] == 13
        assert ch.main_receive(convert='up')['center'] == 7

    def test_inverse_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=6,
                              local_oscillator_frequency=8,
                              bandwidth_channel=1)

        assert ch.main_receive(convert='inverse')['center'] == 2
        assert ch.image_receive(convert='inverse')['center'] == 14

    def test_lo_harmonics(self):
        ch = ReceiveRFChannel(intermediate_frequency=10,
                              local_oscillator_frequency=3,
                              bandwidth_channel=1)
        lo_harm = ch.get_lo_harmonics()
        assert lo_harm['3HLO'] == 9
